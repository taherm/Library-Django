# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('mem_id', models.IntegerField(max_length=7, primary_key=True, serialize=False)),
                ('mem_name', models.CharField(max_length=50)),
                ('mem_addr', models.CharField(max_length=70)),
                ('mem_reg', models.DateField()),
                ('mem_exp', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
