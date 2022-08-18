from django.urls import path

from .views import *
urlpatterns = [
    path('cadastrar/apto/',     AptoCreate.as_view(), name = 'cadastrar-apto'),
    path('cadastrar/tipo/',     TipoCreate.as_view(), name = 'cadastrar-tipo'),
    path('cadastrar/item/',     ItemCreate.as_view(), name = 'cadastrar-item'),
    path('cadastrar/registro/', RegistroCreate.as_view(), name = 'cadastrar-registro'),
    
    path('editar/apto/<int:pk>',     AptoUpdate.as_view(), name = 'editar-apto'),
    path('editar/tipo/<int:pk>',     TipoUpdate.as_view(), name = 'editar-tipo'),
    path('editar/item/<int:pk>',     ItemUpdate.as_view(), name = 'editar-item'),
    path('editar/registro/<int:pk>', RegistroUpdate.as_view(), name = 'editar-registro'),
    
    path('excluir/apto/<int:pk>',     AptoDelete.as_view(), name = 'excluir-apto'),
    path('excluir/tipo/<int:pk>',     TipoDelete.as_view(), name = 'excluir-tipo'),
    path('excluir/item/<int:pk>',     ItemDelete.as_view(), name = 'excluir-item'),
    path('excluir/registro/<int:pk>', RegistroDelete.as_view(), name = 'excluir-registro'),
    
    path('listar/apto/',     AptoList.as_view(), name = 'listar-apto'),
    path('listar/tipo/',     TipoList.as_view(), name = 'listar-tipo'),
    path('listar/item/',     ItemList.as_view(), name = 'listar-item'),
    path('listar/registro/', RegistroList.as_view(), name = 'listar-registro'),
    

]
