# Generated by Django 2.2 on 2020-01-27 07:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dice_hero_app', '0008_auto_20200126_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armor',
            name='defense',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='attack',
        ),
        migrations.AddField(
            model_name='armor',
            name='atk_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='armor',
            name='def_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='armor',
            name='hp_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='armor',
            name='int_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='armor',
            name='spd_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='weapon',
            name='atk_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='weapon',
            name='def_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='weapon',
            name='hp_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='weapon',
            name='int_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
        migrations.AddField(
            model_name='weapon',
            name='spd_boost',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
    ]
