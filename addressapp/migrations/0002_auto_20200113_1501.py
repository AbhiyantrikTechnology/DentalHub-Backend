# Generated by Django 2.1 on 2020-01-13 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='category',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ward',
            name='name',
            field=models.CharField(db_index=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='ward',
            name='ward',
            field=models.PositiveIntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='ward_number'),
        ),
    ]
