# Generated by Django 4.0.3 on 2022-05-31 09:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')], unique=True)),
                ('from_hour', models.TimeField(default=datetime.time(9, 0))),
                ('to_hour', models.TimeField(default=datetime.time(18, 0))),
            ],
            options={
                'verbose_name': 'Расписание магазина',
                'verbose_name_plural': 'Расписание магазинов',
                'ordering': ['weekday'],
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название улицы')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appshop.city', verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название магазина')),
                ('house_number', models.PositiveIntegerField(verbose_name='Номер дома')),
                ('isOpened', models.BooleanField(default=False)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='appshop.city')),
                ('schedule', models.ManyToManyField(to='appshop.schedule', verbose_name='Расписание магазина')),
                ('street', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appshop.street')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
    ]