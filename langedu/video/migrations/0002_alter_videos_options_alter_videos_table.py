# Generated by Django 4.2.4 on 2023-08-11 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videos',
            options={'managed': True, 'verbose_name': 'Видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.AlterModelTable(
            name='videos',
            table='videos',
        ),
    ]
