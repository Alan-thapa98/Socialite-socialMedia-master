# Generated by Django 3.1.1 on 2020-09-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0009_chat_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='user_requested',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='user_requesting',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='owner',
            field=models.CharField(default='', max_length=900),
            preserve_default=False,
        ),
    ]
