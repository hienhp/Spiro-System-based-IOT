# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lung_function', '0003_fef_fev1_fvc_pef'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lungequation',
            old_name='error',
            new_name='ms_error',
        ),
        migrations.AddField(
            model_name='lungequation',
            name='dataset_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='lungequation',
            name='proportion',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='lungequation',
            name='test_err',
            field=models.FloatField(null=True),
        ),
    ]
