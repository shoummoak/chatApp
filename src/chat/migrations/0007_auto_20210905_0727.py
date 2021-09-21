# Generated by Django 3.2.6 on 2021-09-05 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20210905_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='datetime',
        ),
        migrations.AddField(
            model_name='message',
            name='receiver_user',
            field=models.CharField(default='dummy', max_length=500),
        ),
        migrations.AddField(
            model_name='message',
            name='sender_user',
            field=models.CharField(default='dummy', max_length=500),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(default='dummy', max_length=500),
        ),
    ]