from django.urls import path
from autenticacao.views import autenticacao_views

urlpatterns = [
    path('login/', autenticacao_views.login_usuario, name='login'),
    path('logout/', autenticacao_views.logout_usuario, name='logout'),
]