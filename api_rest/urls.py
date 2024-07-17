from django.urls import path
from .views import *



urlpatterns = [
    path('', home),
    path('cadastrar/',cadastrar, name='cadastrar'),
    path('salvar/', salvar, name='salvar'),
    path('login/', login , name='login'),
    path('Logar/', logar, name='logar'),
    path('homeLog/', homeLog, name='homeLog'),
    path('editar/<int:id>',editar,name='editar'),
    path('update/<int:id>',update , name='update'),
    path('delete/<int:id>',delete ,name='delete'),
    path('listar/', listar, name='listar'),
    path('logout/', custom_logout, name='logout'),
    # path('user_list_json/', user_list_json, name='user_list_json'),
]
