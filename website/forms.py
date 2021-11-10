from helloworld.models import Curso
from helloworld.models import Usuario
from django import forms


# FORMULÁRIO DE INCLUSÃO DE CURSOS
# -------------------------------------------

class InsereCursoForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Curso

        # Campos que estarão no form
        fields = [
            'nome',
            'universidade'           
        ]


# FORMULÁRIO DE INCLUSÃO DE USUARIOS
# -------------------------------------------

class InsereUsuarioForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Usuario

        # Campos que estarão no form
        fields = [
            'nome',
            'email', 
        
        ]
