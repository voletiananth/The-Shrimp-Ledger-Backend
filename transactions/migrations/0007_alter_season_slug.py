# Generated by Django 4.0.4 on 2022-05-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_alter_season_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]