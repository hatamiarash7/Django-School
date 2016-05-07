# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='unitselect',
            options={'ordering': ('lesson_code', 'student_code')},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='capacity',
            field=models.CharField(max_length=20, verbose_name='ظرفیت ', null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='cno',
            field=models.CharField(max_length=20, verbose_name='شماره کلاس ', null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='hour',
            field=models.CharField(max_length=20, verbose_name='ساعت ', null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='uno',
            field=models.CharField(max_length=20, verbose_name='تعداد واحد ', null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teach_hour',
            field=models.CharField(max_length=20, verbose_name='ساعت تدریس ', null=True),
        ),
    ]
