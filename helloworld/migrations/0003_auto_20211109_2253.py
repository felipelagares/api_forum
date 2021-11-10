# Generated by Django 3.2.7 on 2021-11-10 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_auto_20211020_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='universidade',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.CharField(help_text='Digite sua resposta de no máximo 1000 caracteres', max_length=1000),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(help_text='Digite o nome do curso', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='universidade',
            field=models.CharField(help_text='Digite a Universidade do curso', max_length=100),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='nome',
            field=models.CharField(help_text='Digite o nome da disciplina', max_length=100),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nivel',
            field=models.CharField(help_text='Digite o nível', max_length=5),
        ),
        migrations.AlterField(
            model_name='topico',
            name='nome',
            field=models.CharField(help_text='Digite o nome do tópico', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(help_text='Digite o email do usuário', max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(help_text='Digite o nome completo', max_length=100),
        ),
    ]
