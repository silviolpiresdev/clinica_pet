from funcionarios.models import Funcionario

def listar_funcionarios():
    return Funcionario.objects.all()

def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(
        nome=funcionario.nome,
        nascimento=funcionario.nascimento,
        cargo=funcionario.cargo,
        username=funcionario.username,
        password=funcionario.password
    )