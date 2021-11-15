# Generated by Django 3.2.9 on 2021-11-15 08:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=255)),
                ('postcode', models.CharField(max_length=20)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address', models.CharField(max_length=80)),
                ('club_opening_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
