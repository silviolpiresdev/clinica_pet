from django.urls import path
from consultas.views import consulta_pet_views

urlpatterns = [
    path('cadastrar_consulta/<int:id>', consulta_pet_views.inserir_consulta, name='cadastrar_consulta'),
    path('lista_consulta/<int:id>', consulta_pet_views.listar_consulta_id, name='listar_consulta_id'),
]