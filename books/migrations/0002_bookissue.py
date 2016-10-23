# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('IssueId', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('IssueDate', models.DateField()),
                ('ReturnDate', models.DateField()),
                ('Book', models.ForeignKey(to='books.Book')),
                ('MemId', models.ForeignKey(to='members.Members')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
