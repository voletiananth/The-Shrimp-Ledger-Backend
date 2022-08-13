from django.contrib.auth.models import User
from django.db import models
from theshrimpledger.settings import AUTH_USER_MODEL
from theshrimpledger.utils import auto_slug
from transactions.models import Season


# Create your models here.
@auto_slug()
class Seed(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    season = models.OneToOneField(Season, on_delete=models.CASCADE, default=0)
    cost = models.DecimalField(decimal_places=2, max_digits=20)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'seed'
        ordering = ['-date_created']


@auto_slug()
class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200, null=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=20)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'medicine'
        ordering = ['-date_created']


@auto_slug()
class Feed(models.Model):
    PAYMENT_CHOICES = [
        ('CH', 'Cash'),
        ('CT', 'Credit')
    ]

    TYPES = [
        ('1MG', '1mg'),
        ('2MG', '2mg')
    ]

    id = models.AutoField(primary_key=True)
    bags = models.IntegerField()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    per_cost = models.DecimalField(decimal_places=2, max_digits=20, default=0.0, blank=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    type = models.CharField(max_length=20, choices=TYPES)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'feed'
        ordering = ['-date_created']


@auto_slug()
class Oil(models.Model):
    id = models.AutoField(primary_key=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    liters = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'oil'
        ordering = ['-date_created']


@auto_slug()
class Repair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="", blank=True)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'repair'
        ordering = ['-date_created']


@auto_slug()
class Miscellaneous(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="", null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'miscellaneous'
        ordering = ['-date_created']
