# Generated by Django 3.2.7 on 2021-11-10 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0004_auto_20211109_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
    ]
