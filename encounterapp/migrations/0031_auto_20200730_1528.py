# Generated by Django 2.1 on 2020-07-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encounterapp', '0030_encounter_request_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modifydelete',
            name='modify_status',
            field=models.CharField(choices=[('pending', 'Pending '), ('approved', 'Approved'), ('rejected', 'Rejected'), ('modified', 'Modified'), ('expired', 'Expired')], default='', max_length=100),
        ),
    ]
