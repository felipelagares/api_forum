# Generated by Django 3.2.7 on 2021-11-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0007_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(help_text='Digite o email do usuário', max_length=254, unique=True),
        ),
    ]
