# Generated by Django 2.1 on 2020-07-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encounterapp', '0024_auto_20200710_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='created_at',
            field=models.DateTimeField(db_index=True),
        ),
    ]
