# Generated by Django 5.0.3 on 2024-03-17 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rs_auth', '0004_remove_vehiclefares_modelname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_location', models.CharField(max_length=255)),
                ('drop_location', models.CharField(max_length=255)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('driver_id', models.CharField(max_length=255)),
                ('vehicletype', models.CharField(max_length=255)),
                ('vehicleregnum', models.CharField(max_length=255)),
                ('base_fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_status', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rs_auth.normaluser')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedbackcomments', models.CharField(max_length=255)),
                ('starRating', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rs_auth.normaluser')),
            ],
        ),
    ]
