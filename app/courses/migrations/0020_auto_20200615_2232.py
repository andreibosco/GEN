# Generated by Django 3.0.7 on 2020-06-15 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20200615_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='show_thumbnails',
            field=models.BooleanField(default=True, help_text='* FOR VIDEO AND UPLOAD SECTIONS ONLY *: enables displaying video thumbnails.', verbose_name='show thumbnails'),
        ),
    ]