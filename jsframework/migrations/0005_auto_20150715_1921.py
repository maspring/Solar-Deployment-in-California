# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0004_auto_20150715_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='city',
            field=models.CharField(default='0.0', max_length=255, null=True),
        ),
    ]
