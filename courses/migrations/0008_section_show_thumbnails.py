# Generated by Django 3.0.7 on 2020-06-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20200523_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='show_thumbnails',
            field=models.BooleanField(default=True, help_text='* FOR VIDEO SECTION ONLY *: enables displaying video thumbnails.'),
        ),
    ]