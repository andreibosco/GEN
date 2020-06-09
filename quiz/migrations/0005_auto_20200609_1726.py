# Generated by Django 3.0.3 on 2020-06-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_question_multiple_correct_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('H', 'Header'), ('L', 'Likert'), ('O', 'Open ended'), ('M', 'Multiple choice')], max_length=1),
        ),
    ]
