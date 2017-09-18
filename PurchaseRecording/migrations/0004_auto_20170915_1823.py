# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-15 18:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseRecording', '0003_auto_20170915_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentinfo',
            name='payment_id',
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='paid_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PurchaseRecording.CreditCard'),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='payment_date',
            field=models.DateField(default=datetime.date(2017, 9, 15)),
        ),
    ]
