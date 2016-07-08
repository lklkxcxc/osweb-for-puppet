# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osweb', '0003_auto_20160504_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='class_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='end_time',
            field=models.DateTimeField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
