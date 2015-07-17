# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0007_auto_20150715_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='azimuth',
            field=models.CharField(default=b'None', max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='seller',
            field=models.CharField(default=b'None', max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='tilt',
            field=models.CharField(default=b'None', max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='tracking',
            field=models.CharField(default=b'None', max_length=256, null=True, blank=True),
        ),
    ]
