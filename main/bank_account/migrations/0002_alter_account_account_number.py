# Generated by Django 4.2.6 on 2023-11-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default='random', max_length=20),
        ),
    ]
