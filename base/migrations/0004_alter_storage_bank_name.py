# Generated by Django 4.1.1 on 2022-09-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_storage_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='bank_name',
            field=models.CharField(choices=[('Kuda', 'Kuda Bank'), ('Zenith', 'Zenith Bank'), ('Guarantee Trust', 'Guarantee Trust Bank'), ('First', 'First Bank'), ('Stanbic IBTC', 'Stanbic IBTC Bank'), ('Sterling', 'Sterling Bank')], max_length=50),
        ),
    ]
