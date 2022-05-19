# Generated by Django 4.0.4 on 2022-05-14 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('slug', models.SlugField(auto_created=True, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'season',
                'ordering': ['-date_created'],
            },
        ),
    ]
