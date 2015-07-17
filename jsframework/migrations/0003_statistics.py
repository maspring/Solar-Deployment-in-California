# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0002_auto_20150703_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(unique=True, max_length=256)),
                ('totalProduction', models.FloatField(max_length=256, null=True, blank=True)),
                ('city', models.CharField(default='0.0', max_length=10, null=True)),
                ('totalDeployments', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('costOhSix', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionOhSix', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattOhSix', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsOhSix', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costOhSeven', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionOhSeven', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattOhSeven', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsOhSeven', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costOhEight', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionOhEight', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattOhEight', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsOhEight', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costOhNine', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionOhNine', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattOhNine', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsOhNine', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costTen', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionTen', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattTen', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsTen', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costEleven', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionEleven', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattEleven', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsEleven', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costTwelve', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionTwelve', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattTwelve', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsTwelve', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costThirteen', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionThirteen', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattThirteen', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsThirteen', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costFourteen', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionFourteen', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattFourteen', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsFourteen', models.IntegerField(max_length=10, null=True, blank=True)),
                ('costFifteen', models.FloatField(default='0.0', max_length=10, null=True, blank=True)),
                ('productionFifteen', models.FloatField(max_length=10, null=True, blank=True)),
                ('costPerWattFifteen', models.FloatField(max_length=10, null=True, blank=True)),
                ('deploymentsFifteen', models.IntegerField(max_length=10, null=True, blank=True)),
            ],
        ),
    ]
