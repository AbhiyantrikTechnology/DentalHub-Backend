# Generated by Django 2.1 on 2020-08-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encounterapp', '0034_auto_20200810_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modifydelete',
            name='other_reason_for_deletion',
            field=models.TextField(null=True),
        ),
    ]
