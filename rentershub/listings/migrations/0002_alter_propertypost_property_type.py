# Generated by Django 5.0.3 on 2024-08-29 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertypost',
            name='property_type',
            field=models.CharField(choices=[('House', 'HOUSE'), ('Guest Wing', 'GUEST WING'), ('Quarters', 'QUARTERS'), ('Hostel', 'HOSTEL'), ('Flat', 'FLAT')], default='House', max_length=20),
        ),
    ]
