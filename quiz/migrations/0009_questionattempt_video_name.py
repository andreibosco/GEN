# Generated by Django 3.0.3 on 2020-06-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20200610_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionattempt',
            name='video_name',
            field=models.TextField(blank=True, null=True, verbose_name='video file original name'),
        ),
    ]