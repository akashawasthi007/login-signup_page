# Generated by Django 3.2 on 2021-05-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usr',
            name='gender',
            field=models.CharField(default='M', max_length=1),
        ),
    ]