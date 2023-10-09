# Generated by Django 4.2.5 on 2023-10-04 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwiji_app', '0031_alter_posts_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='gwiji_app.campaigns'),
        ),
    ]
