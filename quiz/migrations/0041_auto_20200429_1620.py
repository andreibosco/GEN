# Generated by Django 3.0.3 on 2020-04-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0040_auto_20200429_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mcanswer',
            options={'ordering': ['order'], 'verbose_name': 'Multiple choice answer', 'verbose_name_plural': 'Multiple choice answers'},
        ),
        migrations.AddField(
            model_name='mcanswer',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
