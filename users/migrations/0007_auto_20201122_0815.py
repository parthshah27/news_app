# Generated by Django 3.1.3 on 2020-11-22 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_appuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appuser',
            options={'verbose_name': 'App User', 'verbose_name_plural': 'App Users'},
        ),
    ]