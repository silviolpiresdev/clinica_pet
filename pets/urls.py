from django.urls import path
from .views import pet_views

urlpatterns = [
    path('inserir/<int:id>', pet_views.inserir_pet, name='cadastrar_pet'),
    path('detalhe/<int:id>', pet_views.listar_pet_id, name='listar_pet_id'),
    path('editar/<int:id>', pet_views.editar_pet, name='editar_pet'),
]