# Generated by Django 2.2.3 on 2019-09-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0009_userprofile_timer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='choice',
        ),
        migrations.AddField(
            model_name='submission',
            name='choice',
            field=models.CharField(default='cpp', max_length=5),
        ),
    ]