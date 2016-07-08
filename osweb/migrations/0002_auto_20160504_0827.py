# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='filesystem',
            field=models.CharField(max_length=2400, null=True),
        ),
    ]
