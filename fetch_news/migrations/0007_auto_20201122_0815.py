# Generated by Django 3.1.3 on 2020-11-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_news', '0006_article_bulk_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
