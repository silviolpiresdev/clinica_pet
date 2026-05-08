from consultas.models import ConsultaPet

def cadastrar_consulta(consulta):
    ConsultaPet.objects.create(
        pet=consulta.pet,
        motivo_consulta=consulta.motivo_consulta,
        peso_atual=consulta.peso_atual,
        medicamento_atual=consulta.medicamento_atual,
        medicamentos_prescritos=consulta.medicamentos_prescritos,
        exames_prescritos=consulta.exames_prescritos
    )

def listar_consultas(id):
    return ConsultaPet.objects.filter(pet=id).all()

def listar_consultas_pets(id):
    return ConsultaPet.objects.filter(pet__dono=id).all().order_by('-data')

def listar_consulta(id):
    return ConsultaPet.objects.get(id=id)