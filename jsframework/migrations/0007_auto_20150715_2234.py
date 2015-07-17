# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0006_auto_20150715_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='application',
            field=models.CharField(max_length=256),
        ),
    ]
