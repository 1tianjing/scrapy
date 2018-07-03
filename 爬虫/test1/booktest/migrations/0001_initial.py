# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpubdate', models.DateTimeField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Heroinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('hname', models.CharField(max_length=20)),
                ('hsex', models.BooleanField(default=True)),
                ('hcontent', models.TextField(max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
                ('hbook', models.ForeignKey(to='booktest.Bookinfo')),
            ],
            options={
                'db_table': 'heroinfo',
            },
        ),
    ]
