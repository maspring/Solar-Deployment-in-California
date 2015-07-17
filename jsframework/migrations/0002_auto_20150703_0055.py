# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='cost',
            field=models.FloatField(default='0.0', max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='firstdate',
            field=models.DateField(default='1960-01-01', blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='fourthdate',
            field=models.DateField(default='1960-01-01', blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='incentive',
            field=models.FloatField(default='0.0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='rating',
            field=models.FloatField(default='0.0', max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='seconddate',
            field=models.DateField(default='1960-01-01', blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='seller',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='thirddate',
            field=models.DateField(default='1960-01-01', blank=True),
        ),
    ]
