# Generated by Django 4.2.6 on 2023-11-24 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_delete_card'),
        ('bank_account', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
