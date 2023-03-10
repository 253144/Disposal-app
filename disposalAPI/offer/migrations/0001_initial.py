# Generated by Django 4.1.5 on 2023-01-21 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=100)),
                ('update_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('size', models.FloatField()),
                ('type', models.TextField()),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.price')),
            ],
        ),
    ]
