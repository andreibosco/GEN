# Generated by Django 3.0.7 on 2020-06-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20200615_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='create_discussions',
            field=models.BooleanField(default=False, help_text="* FOR UPLOAD SECTION ONLY *: automatically create a discussion board based on participant's video submissions.", verbose_name='create discussion'),
        ),
    ]
