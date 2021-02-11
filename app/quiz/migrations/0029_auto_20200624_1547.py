# Generated by Django 3.0.7 on 2020-06-24 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0028_auto_20200624_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionattempt',
            name='multiplechoice_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='quiz.MCAnswer', verbose_name='multiple choice answer item'),
        ),
    ]