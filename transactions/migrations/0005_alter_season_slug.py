# Generated by Django 4.0.4 on 2022-05-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='slug',
            field=models.SlugField(allow_unicode=True, auto_created=True, default='djangodbmodelsfieldsautofield'),
        ),
    ]