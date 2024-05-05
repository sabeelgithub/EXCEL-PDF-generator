# Generated by Django 5.0.4 on 2024-05-03 08:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payer', models.CharField(blank=True, max_length=20)),
                ('receiver', models.CharField(blank=True, max_length=20)),
                ('amount', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=20)),
                ('project', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(blank=True, default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('transaction_date', models.DateField(null=True)),
                ('is_check', models.BooleanField(default=False)),
            ],
        ),
    ]
