# Generated by Django 3.0.7 on 2020-06-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0022_auto_20200615_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='likertanswer',
            name='legend_en',
            field=models.TextField(blank=True, help_text='Legend for the likert scale values.', null=True, verbose_name='legend'),
        ),
        migrations.AddField(
            model_name='likertanswer',
            name='legend_fr',
            field=models.TextField(blank=True, help_text='Legend for the likert scale values.', null=True, verbose_name='legend'),
        ),
    ]
