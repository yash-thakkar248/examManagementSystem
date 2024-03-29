# Generated by Django 4.1.13 on 2024-03-15 00:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Name can only contain letters', regex='^[a-zA-Z]+$')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Name can only contain letters', regex='^[a-zA-Z]+$')])),
                ('username', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message='Username can only contain letters, numbers, and ._-', regex='^[a-zA-Z0-9._-]+$')])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid email address', regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')])),
                ('password', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Password must contain at least 8 characters, including uppercase, lowercase, numbers, and special characters', regex='^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=\\-{}[\\]:;"\\\'|,.<>/?]).{8,}$')])),
                ('user_type', models.CharField(max_length=150)),
            ],
        ),
    ]
