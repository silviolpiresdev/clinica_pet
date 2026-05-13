from django.contrib.auth.models import AbstractUser
from django.db import models

class Funcionario(AbstractUser):
    CARGO_CHOICES = [
        (1, 'Veterinario'),
        (2, 'Financeiro'),
        (3, 'Atendimento'),
    ]
    nome = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'funcionario'