# Generated by Django 3.1.3 on 2020-11-28 19:49

from django.db import migrations
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20201124_1439'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', registration.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
