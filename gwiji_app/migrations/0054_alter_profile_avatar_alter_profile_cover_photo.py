# Generated by Django 4.2.5 on 2023-10-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwiji_app', '0053_campaigns_intented_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='profile_cover'),
        ),
    ]
