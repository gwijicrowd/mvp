# Generated by Django 4.2.5 on 2023-10-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwiji_app', '0015_projects_financials_doc_projects_legals_doc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='operational_doc',
            field=models.FileField(default='', upload_to='market_research_doc'),
        ),
    ]
