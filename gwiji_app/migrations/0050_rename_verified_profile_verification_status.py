# Generated by Django 4.2.5 on 2023-10-15 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwiji_app', '0049_remove_profile_profile_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='verified',
            new_name='verification_status',
        ),
    ]
