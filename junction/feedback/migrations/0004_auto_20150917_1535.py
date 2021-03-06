# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20150913_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicefeedbackquestion',
            name='is_required',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textfeedbackquestion',
            name='is_required',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
