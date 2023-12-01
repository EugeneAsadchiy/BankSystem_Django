# Generated by Django 4.2.6 on 2023-12-01 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_card_expiry_years'),
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='linked_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.card', verbose_name='Связанная карточка'),
        ),
    ]
