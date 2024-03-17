# Generated by Django 5.0.2 on 2024-03-17 04:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rs_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 17, 4, 22, 36, 976707, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 17, 4, 22, 39, 917067, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicletype',
            field=models.CharField(default=datetime.datetime(2024, 3, 17, 4, 22, 43, 125186, tzinfo=datetime.timezone.utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='normaluser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 17, 4, 22, 46, 402406, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='normaluser',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 17, 4, 22, 48, 802436, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driver',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phonenumber',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='phonenumber',
            field=models.CharField(max_length=20),
        ),
    ]