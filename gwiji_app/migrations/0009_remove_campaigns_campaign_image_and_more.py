# Generated by Django 4.2.5 on 2023-10-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwiji_app', '0008_posts_no_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaigns',
            name='campaign_image',
        ),
        migrations.AddField(
            model_name='campaigns',
            name='campaign_picture',
            field=models.ImageField(blank=True, upload_to='campaign_pictures'),
        ),
    ]
