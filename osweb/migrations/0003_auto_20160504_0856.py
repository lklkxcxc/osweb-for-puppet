# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osweb', '0002_auto_20160504_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='bond_mode',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='boot',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='cpu',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='init',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='lang',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='mem',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='swap',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='timezone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='tmout',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='toptea',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
