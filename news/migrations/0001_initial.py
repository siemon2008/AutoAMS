# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 13:44
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='\u7f51\u5740')),
                ('author', models.CharField(max_length=256, verbose_name='\u4f5c\u8005')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u5185\u5bb9')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5217\u8868',
                'verbose_name_plural': '\u6587\u7ae0\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u680f\u76ee\u540d\u79f0')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='\u680f\u76ee\u7f51\u5740')),
                ('intro', models.TextField(default='', verbose_name='\u680f\u76ee\u7b80\u4ecb')),
                ('nav_display', models.BooleanField(default=False, verbose_name='\u5bfc\u822a\u663e\u793a')),
                ('home_display', models.BooleanField(default=False, verbose_name='\u9996\u9875\u663e\u793a')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u6587\u7ae0\u5206\u7c7b',
                'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Column', verbose_name='\u5206\u7c7b'),
        ),
    ]