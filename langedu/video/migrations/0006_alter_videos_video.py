# Generated by Django 4.2.4 on 2023-08-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_alter_videos_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]