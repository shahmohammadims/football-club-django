# Generated by Django 4.0.6 on 2022-07-26 16:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('9[9]{9}')]),
        ),
    ]
