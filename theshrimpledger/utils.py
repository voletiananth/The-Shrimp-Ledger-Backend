import math
import string
import sys
import time

from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
import random


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return str(random.randint(0, 10000) + math.floor(time.time())) + ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = "slug" + random_string_generator(size=4)
    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def auto_slug():
    def decorator(model):
        assert hasattr(model, "slug"), "Model is missing a slug field"

        @receiver(models.signals.pre_save, sender=model, weak=False)
        def generate_slug(sender, instance, *args, raw=False, **kwargs):

            if not raw and not instance.slug:
                slug = unique_slug_generator(instance)
                if slug:  # not all strings result in a slug value
                    instance.slug = slug

        return model

    return decorator
