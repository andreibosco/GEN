# Generated by Django 3.1.3 on 2020-11-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0040_auto_20201120_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionitem',
            name='show_related_content',
            field=models.BooleanField(default=False, help_text='Display content related to the section items (e.g., quizzes related to a video)', verbose_name='show related content'),
        ),
        migrations.AlterField(
            model_name='sectionitem',
            name='description',
            field=models.TextField(blank=True, help_text='Brief description (max 400 characters)', max_length=400, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='sectionitem',
            name='description_en',
            field=models.TextField(blank=True, help_text='Brief description (max 400 characters)', max_length=400, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='sectionitem',
            name='description_fr',
            field=models.TextField(blank=True, help_text='Brief description (max 400 characters)', max_length=400, null=True, verbose_name='description'),
        ),
    ]
