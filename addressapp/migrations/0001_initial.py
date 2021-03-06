# Generated by Django 2.0 on 2019-09-25 07:37

import addressapp.models.address
import addressapp.models.geography
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.BooleanField(default=True)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='addressapp.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.CharField(default=addressapp.models.address.keygenerator, editable=False, max_length=200, primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=50)),
                ('municipality', models.CharField(max_length=50)),
                ('municipality_type', models.CharField(max_length=50)),
                ('ward', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)], verbose_name='ward_number')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.CharField(default=addressapp.models.geography.keygenerator, editable=False, max_length=200, primary_key=True, serialize=False)),
                ('tole', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressapp.District')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)], verbose_name='ward_number')),
                ('status', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressapp.Municipality')),
            ],
        ),
        migrations.AddField(
            model_name='geography',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressapp.Ward'),
        ),
    ]
