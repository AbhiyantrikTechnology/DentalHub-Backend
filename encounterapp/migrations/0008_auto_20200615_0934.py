# Generated by Django 2.1 on 2020-06-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encounterapp', '0007_auto_20200615_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='reason_for_modification',
            field=models.TextField(default='there was mistake'),
        ),
    ]