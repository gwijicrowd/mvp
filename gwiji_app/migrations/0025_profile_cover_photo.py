# Generated by Django 4.2.5 on 2023-10-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwiji_app', '0024_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='profile_cover'),
        ),
    ]
