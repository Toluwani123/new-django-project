# Generated by Django 4.1.1 on 2022-09-10 21:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_storage_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='account_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)]),
        ),
    ]
