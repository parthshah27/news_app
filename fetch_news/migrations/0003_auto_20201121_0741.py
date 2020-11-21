# Generated by Django 3.1.3 on 2020-11-21 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_news', '0002_auto_20201121_0645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='newsapi',
            options={'verbose_name': 'NewsAPI', 'verbose_name_plural': 'NewsAPIs'},
        ),
        migrations.CreateModel(
            name='MapDBParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_parameter', models.CharField(max_length=100)),
                ('db_parameter', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('news_api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_db_parameter', to='fetch_news.newsapi')),
            ],
        ),
    ]