# Generated by Django 2.0 on 2019-09-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='recall_geography',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]