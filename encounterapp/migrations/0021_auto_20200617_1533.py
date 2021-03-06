# Generated by Django 2.1 on 2020-06-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encounterapp', '0020_auto_20200616_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modifydelete',
            name='delete_status',
            field=models.CharField(choices=[('pending', 'Pending '), ('deleted', 'Deleted')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='modifydelete',
            name='modify_status',
            field=models.CharField(choices=[('pending', 'Pending '), ('approved', 'Approved'), ('modified', 'Modified')], default='', max_length=100),
        ),
    ]
