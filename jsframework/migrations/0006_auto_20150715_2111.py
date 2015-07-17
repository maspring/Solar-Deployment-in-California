# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0005_auto_20150715_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='totalDeployments',
            field=models.IntegerField(default='0', null=True, blank=True),
        ),
    ]
