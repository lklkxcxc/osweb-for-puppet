# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(max_length=100)),
                ('class_env', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('module_name', models.CharField(max_length=200)),
                ('env', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('node_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('cpu', models.CharField(max_length=30, null=True)),
                ('mem', models.CharField(max_length=30, null=True)),
                ('ip', models.GenericIPAddressField(null=True)),
                ('netmask', models.GenericIPAddressField(null=True)),
                ('gateway', models.GenericIPAddressField(null=True)),
                ('os_release', models.CharField(max_length=80, null=True)),
                ('pesize', models.CharField(max_length=300, null=True)),
                ('lang', models.CharField(max_length=30, null=True)),
                ('keyboard', models.CharField(max_length=80, null=True)),
                ('timezone', models.CharField(max_length=30, null=True)),
                ('ntp', models.CharField(max_length=300, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('swap', models.CharField(max_length=30, null=True)),
                ('filesystem', models.CharField(max_length=1800, null=True)),
                ('boot', models.CharField(max_length=30, null=True)),
                ('software', models.CharField(max_length=80, null=True)),
                ('security', models.CharField(max_length=100, null=True)),
                ('toptea', models.CharField(max_length=60, null=True)),
                ('init', models.CharField(max_length=30, null=True)),
                ('network_speed', models.CharField(max_length=120, null=True)),
                ('bond_mode', models.CharField(max_length=300, null=True)),
                ('tmout', models.CharField(max_length=30, null=True)),
                ('ulimit', models.CharField(max_length=100, null=True)),
                ('app', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('offline', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Online',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('online', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(max_length=200)),
                ('end_time', models.DateTimeField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('node_name', models.ForeignKey(to='osweb.Node')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='node_name',
            field=models.ForeignKey(to='osweb.Node'),
        ),
    ]
