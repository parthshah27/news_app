# Generated by Django 3.1.3 on 2020-11-21 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=100, unique=True)),
                ('api_url', models.URLField()),
                ('api_parameters', models.CharField(blank=True, max_length=500, null=True)),
                ('api_key_paramter', models.CharField(blank=True, max_length=100, null=True)),
                ('api_key_token', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('categories', models.ManyToManyField(blank=True, related_name='articles', to='fetch_news.Category')),
            ],
        ),
    ]
