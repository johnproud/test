# Generated by Django 3.2.7 on 2021-10-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_gameresult_answered_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameresult',
            name='earned_points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
