# Generated by Django 3.1.5 on 2021-01-20 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanage', '0003_auto_20210116_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='community_banner',
        ),
        migrations.RemoveField(
            model_name='community',
            name='manager',
        ),
    ]
