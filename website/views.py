from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from helloworld.models import Curso
from helloworld.models import Usuario
from website.forms import InsereCursoForm
from website.forms import InsereUsuarioForm

# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE CURSOS
# ----------------------------------------------

class CursoListView(ListView):
    template_name = "website/lista.html"
    model = Curso
    context_object_name = "cursos"


# CADASTRAMENTO DE CURSOS
# ----------------------------------------------

class CursoCreateView(CreateView):
    template_name = "website/cria.html"
    model = Curso
    form_class = InsereCursoForm
    success_url = reverse_lazy("website:lista_cursos")


# ATUALIZAÇÃO DE CURSOS
# ----------------------------------------------

class CursoUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Curso
    fields = '__all__'
    context_object_name = 'curso'
    success_url = reverse_lazy("website:lista_cursos")


# EXCLUSÃO DE CURSOS
# ----------------------------------------------

class CursoDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Curso
    context_object_name = 'curso'
    success_url = reverse_lazy("website:lista_cursos")


# LISTA DE USUARIOS
# ----------------------------------------------

class UsuarioListView(ListView):
    template_name = "website/lista_usuarios.html"
    model = Usuario
    context_object_name = "usuarios"



# CADASTRAMENTO DE USUARIOS
# ----------------------------------------------

class UsuarioCreateView(CreateView):
    template_name = "website/cria_usuario.html"
    model = Usuario
    form_class = InsereUsuarioForm
    success_url = reverse_lazy("website:lista_usuarios")



# ATUALIZAÇÃO DE USUARIOS
# ----------------------------------------------

class UsuarioUpdateView(UpdateView):
    template_name = "website/atualiza_usuario.html"
    model = Usuario
    fields = '__all__'
    context_object_name = 'usuario'
    success_url = reverse_lazy("website:lista_usuarios")



    # EXCLUSÃO DE USUARIOS
# ----------------------------------------------

class UsuarioDeleteView(DeleteView):
    template_name = "website/exclui_usuario.html"
    model = Usuario
    context_object_name = 'usuario'
    success_url = reverse_lazy("website:lista_usuarios")
