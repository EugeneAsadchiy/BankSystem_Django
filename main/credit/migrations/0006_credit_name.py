# Generated by Django 4.2.6 on 2023-12-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0005_credit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='name',
            field=models.CharField(default='Кредит'),
        ),
    ]
