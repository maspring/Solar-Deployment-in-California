# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0003_statistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsEleven',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsFifteen',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsFourteen',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsOhEight',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsOhNine',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsOhSeven',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsOhSix',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsTen',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsThirteen',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deploymentsTwelve',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
