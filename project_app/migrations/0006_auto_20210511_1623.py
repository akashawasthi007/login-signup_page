# Generated by Django 3.2 on 2021-05-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0005_auto_20210511_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usr',
            name='user',
        ),
        migrations.AddField(
            model_name='usr',
            name='username',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='usr',
            name='gender',
            field=models.CharField(max_length=1),
        ),
    ]
