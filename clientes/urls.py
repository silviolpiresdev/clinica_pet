from django.urls import path
from .views import cliente_views

urlpatterns = [
    path('cadastrar/', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar/', cliente_views.listar_clientes, name='listar_clientes'),
    path('detalhe/<int:id>', cliente_views.listar_cliente_id, name='listar_cliente_id'),
    path('editar/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    path('remover/<int:id>', cliente_views.remover_cliente, name='remover_cliente'),
]