# Generated by Django 4.1.1 on 2022-09-26 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justchat', '0002_delete_user_alter_messages_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ['created_at']},
        ),
    ]
