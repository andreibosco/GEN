# Generated by Django 3.0.3 on 2020-05-17 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20200517_2102'),
        ('quiz', '0060_quiz_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'quizzes'},
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='author',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='created',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='custom_order',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='description',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='id',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='name',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='published',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='section',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='show_score',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='start_date',
        ),
        migrations.AddField(
            model_name='quiz',
            name='sectionitem_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.SectionItem'),
            preserve_default=False,
        ),
    ]
