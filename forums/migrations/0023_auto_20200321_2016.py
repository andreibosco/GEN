# Generated by Django 3.0.3 on 2020-03-22 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0022_auto_20200321_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='video',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='forums', to='forums.VideoFile'),
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='kind',
            field=models.CharField(choices=[('PDF', 'PDF Document'), ('YTB', 'Youtube Video')], default='YTB', max_length=3),
        ),
    ]