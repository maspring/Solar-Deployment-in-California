# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application', models.CharField(unique=True, max_length=256)),
                ('utility', models.CharField(max_length=256, null=True, blank=True)),
                ('incentive', models.FloatField(max_length=10, null=True)),
                ('cost', models.FloatField(max_length=10, null=True, blank=True)),
                ('rating', models.FloatField(max_length=10, null=True, blank=True)),
                ('sector', models.CharField(max_length=256, null=True, blank=True)),
                ('city', models.CharField(max_length=256, null=True, blank=True)),
                ('county', models.CharField(max_length=256, null=True, blank=True)),
                ('state', models.CharField(max_length=16, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=15, null=True, blank=True)),
                ('firstdate', models.DateField(null=True, blank=True)),
                ('seconddate', models.DateField(null=True, blank=True)),
                ('thirddate', models.DateField(null=True, blank=True)),
                ('fourthdate', models.DateField(null=True, blank=True)),
                ('seller', models.CharField(max_length=20, null=True, blank=True)),
                ('azimuth', models.CharField(max_length=20, null=True, blank=True)),
                ('tilt', models.CharField(max_length=20, null=True, blank=True)),
                ('tracking', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
    ]
