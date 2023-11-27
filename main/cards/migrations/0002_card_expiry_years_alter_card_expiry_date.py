# Generated by Django 4.2.6 on 2023-11-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='expiry_years',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiry_date',
            field=models.DateField(default='admin check'),
        ),
    ]
