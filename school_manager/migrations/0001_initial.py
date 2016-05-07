# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام درس ')),
                ('code', models.CharField(max_length=100, null=True, verbose_name='کد درس ')),
                ('capacity', models.IntegerField(null=True, verbose_name='ظرفیت ')),
                ('uno', models.IntegerField(null=True, verbose_name='تعداد واحد ')),
                ('cno', models.IntegerField(null=True, verbose_name='شماره کلاس ')),
                ('hour', models.IntegerField(null=True, verbose_name='ساعت ')),
            ],
            options={
                'ordering': ('id', 'name', 'code', 'capacity', 'uno', 'cno', 'hour'),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='نام ')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='نام خانوادگی ')),
                ('birthday', models.CharField(max_length=10, null=True, verbose_name='تاریخ تولد ')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='تلفن ثابت ')),
                ('mobile', models.CharField(max_length=20, null=True, verbose_name='تلفن همراه ')),
                ('stno', models.CharField(max_length=10, null=True, verbose_name='شماره دانشجویی ')),
                ('father_name', models.CharField(max_length=100, null=True, verbose_name='نام پدر ')),
                ('father_job', models.CharField(max_length=100, null=True, verbose_name='شغل پدر ')),
                ('father_phone', models.CharField(max_length=20, null=True, verbose_name='تلفن پدر ')),
                ('id_code', models.CharField(max_length=10, null=True, verbose_name='شماره شناسنامه ')),
                ('national_id', models.CharField(max_length=10, null=True, verbose_name='کد ملی ')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='آدرس ')),
                ('study_field', models.CharField(max_length=100, null=True, verbose_name='رشته تحصیلی ')),
                ('probation', models.BooleanField(default=False, verbose_name='مشروطی ')),
            ],
            options={
                'ordering': ('id', 'first_name', 'last_name', 'stno', 'id_code', 'national_id', 'phone', 'mobile', 'father_name', 'father_phone', 'father_job', 'birthday', 'address', 'study_field', 'probation'),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='نام ')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='نام خانوادگی ')),
                ('tno', models.CharField(max_length=10, null=True, verbose_name='کد ملی ')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='تلفن ثابت ')),
                ('mobile', models.CharField(max_length=20, null=True, verbose_name='تلفن همراه ')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='آدرس ')),
                ('teach_hour', models.IntegerField(null=True, verbose_name='ساعت تدریس ')),
            ],
            options={
                'ordering': ('id', 'first_name', 'last_name', 'tno', 'phone', 'mobile', 'address', 'teach_hour'),
            },
        ),
        migrations.CreateModel(
            name='UnitSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_code', models.ForeignKey(to='school_manager.Lesson')),
                ('student_code', models.ForeignKey(to='school_manager.Student')),
            ],
        ),
    ]
