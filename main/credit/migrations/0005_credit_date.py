# Generated by Django 4.2.6 on 2023-12-02 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0004_remove_credit_linked_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
