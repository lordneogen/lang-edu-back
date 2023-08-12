# Generated by Django 4.2.4 on 2023-08-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.FileField(null=True, upload_to='text/')),
            ],
            options={
                'verbose_name': 'Текста',
                'verbose_name_plural': 'Текст',
                'db_table': 'text',
                'managed': True,
            },
        ),
    ]
