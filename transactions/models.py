from django.contrib.auth.models import User
from django.db import models

from theshrimpledger.utils import autoSlug


@autoSlug()
class Season(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )
    number = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.number != 0:
            super(Season, self).save(*args, **kwargs)
            return
        seasons = Season.objects.filter(user=self.user).count()
        self.number = seasons+1
        super(Season, self).save(*args, **kwargs)

    class Meta:
        db_table = 'season'
        ordering = ['-date_created', '-user']

