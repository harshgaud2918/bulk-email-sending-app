# Generated by Django 4.0.6 on 2022-08-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('company', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('phone', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]