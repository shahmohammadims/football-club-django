# Generated by Django 4.0.6 on 2022-07-26 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_account_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='view_profile',
        ),
    ]