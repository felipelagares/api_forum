from website.views import IndexTemplateView, CursoListView, \
    CursoUpdateView, CursoCreateView, CursoDeleteView, UsuarioCreateView, UsuarioListView, UsuarioUpdateView, UsuarioDeleteView
from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /curso/cadastrar
    path('curso/cadastrar', CursoCreateView.as_view(), name="cadastra_curso"),

    # GET /curso
    path('cursos/', CursoListView.as_view(), name="lista_cursos"),

    # GET/POST /cursos/{pk}
    path('curso/<pk>', CursoUpdateView.as_view(), name="atualiza_curso"),

    # GET/POST /cursos/excluir/{pk}
    path('curso/excluir/<pk>', CursoDeleteView.as_view(), name="deleta_curso"),

    # GET /usuario/cadastrar
    path('usuarios/cadastrar', UsuarioCreateView.as_view(), name="cadastra_usuario"),

    # GET /usuario
    path('usuarios/', UsuarioListView.as_view(), name="lista_usuarios"),

     # GET/POST /usuarios/{pk}
    path('usuario/<pk>', UsuarioUpdateView.as_view(), name="atualiza_usuario"),

     # GET/POST /usuarios/excluir/{pk}
    path('usuarios/excluir/<pk>', UsuarioDeleteView.as_view(), name="deleta_usuario"),


]
