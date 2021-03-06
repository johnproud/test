# Generated by Django 3.2.7 on 2021-10-08 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_remove_gameresult_responses'),
        ('nomenclatures', '0003_auto_20211008_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='responses', to='games.game'),
            preserve_default=False,
        ),
    ]
