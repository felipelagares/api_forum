from django.db import models

class Curso(models.Model):
    #o nome do curso deve ser único, não se repete
    nome = models.CharField(max_length=100, help_text="Digite o nome do curso", unique=True)    
    universidade = models.CharField(max_length=100, help_text='Digite a Universidade do curso')
    #Os campos nao podem ficar em branco ou ser nulos
    null = False
    blank = False

class Disciplina(models.Model):
    #o nome da disciplina deve ser único, não se repete
    nome = models.CharField(max_length=100, help_text='Digite o nome da disciplina', unique=True)
    null = False
    blank = False

class Usuario(models.Model):
    nome = models.CharField(max_length=100, help_text='Digite o nome completo')
    #podem existir 2 usuarios com mesmo nome, mas o e-mail é único 
    email = models.EmailField(help_text='Digite o email do usuário', unique=True)
    #data_criacao = models.DateTimeField()
    #universidade = Curso.universidade
    #cursando = Curso
    #Os campos nao podem ficar em branco ou ser nulos
    null = False
    blank = False

class Aluno(Usuario):
    curso = Curso


class Professor(Usuario):
    nivel = models.CharField(max_length=5, help_text='Digite o nível')
    #Os campos nao podem ficar em branco ou ser nulos
    null = False
    blank = False

class Comentario(models.Model):
    autor = Usuario
    data_criacao = models.DateTimeField()
    texto = models.CharField(max_length=1000, help_text='Digite sua resposta de no máximo 1000 caracteres')
    #Os campos nao podem ficar em branco ou ser nulos
    null = False
    blank = False

class Topico(models.Model):
    nome = models.CharField(max_length=100, help_text='Digite o nome do tópico', unique=True)
    data_criacao = models.DateTimeField()
    autor = Usuario
    #Os campos nao podem ficar em branco ou ser nulos
    null = False
    blank = False

objetos = models.Manager()