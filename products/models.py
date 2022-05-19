from django.contrib.auth.models import User
from django.db import models

from theshrimpledger.utils import autoSlug
from transactions.models import Season


# Create your models here.
@autoSlug()
class Seed(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    season = models.OneToOneField(Season, on_delete=models.CASCADE, default=0)
    cost = models.DecimalField(decimal_places=2, max_digits=20)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'seed'
        ordering = ['-date_created']


@autoSlug()
class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=20)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'medicine'
        ordering = ['-date_created']


@autoSlug()
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    per_cost = models.DecimalField(decimal_places=2, max_digits=20, default=0.0, null=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    type = models.CharField(max_length=20, choices=TYPES)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'feed'
        ordering = ['-date_created']


@autoSlug()
class Oil(models.Model):
    id = models.AutoField(primary_key=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    liters = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'oil'
        ordering = ['-date_created']


@autoSlug()
class Repair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="", null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'repair'
        ordering = ['-date_created']


@autoSlug()
class Miscellaneous(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="", null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True, )

    class Meta:
        db_table = 'miscellaneous'
        ordering = ['-date_created']
