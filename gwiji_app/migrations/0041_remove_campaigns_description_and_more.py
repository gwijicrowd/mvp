# Generated by Django 4.2.5 on 2023-10-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwiji_app', '0040_alter_investments_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaigns',
            name='description',
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='subtitle',
            field=models.CharField(max_length=200),
        ),
    ]
