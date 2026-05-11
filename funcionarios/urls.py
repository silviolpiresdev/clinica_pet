from django.urls import path
from .views import funcionario_views

urlpatterns = [
    path('inserir/', funcionario_views.inserir_funcionario, name='cadastrar_funcionario'),
    path('detalhe/', funcionario_views.listar_funcionarios, name='listar_funcionarios'),
    ]