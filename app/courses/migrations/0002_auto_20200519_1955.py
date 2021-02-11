# Generated by Django 3.0.3 on 2020-05-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(help_text='Course description (max 400 characters)', max_length=400),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True, help_text='Course description (max 200 characters)', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sectionitem',
            name='description',
            field=models.TextField(help_text='Brief description (max 200 characters)', max_length=200),
        ),
    ]