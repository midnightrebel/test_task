# Generated by Django 4.0.3 on 2022-06-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название улицы'),
        ),
    ]