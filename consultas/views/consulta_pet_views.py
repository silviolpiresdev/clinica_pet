from django.shortcuts import redirect, render
from consultas.forms.consulta_pet_form import ConsultaPetForm
from consultas.services import consulta_pet_service
from consultas.entidades.consulta_pet import ConsultaPet
from pets.services import pet_service

def inserir_consulta(request, id):
    if request.method == 'POST':
        form_consulta = ConsultaPetForm(request.POST)
        pet = pet_service.listar_pet_id(id)
        if form_consulta.is_valid():
            consulta_nova = ConsultaPet(
                pet=pet,
                motivo_consulta=form_consulta.cleaned_data['motivo_consulta'],
                peso_atual=form_consulta.cleaned_data['peso_atual'],
                medicamento_atual=form_consulta.cleaned_data['medicamento_atual'],
                medicamentos_prescritos=form_consulta.cleaned_data['medicamentos_prescritos'],
                exames_prescritos=form_consulta.cleaned_data['exames_prescritos'],
            )
            consulta_pet_service.cadastrar_consulta(consulta_nova)
            return redirect('listar_pet_id', pet.id)
    else:
        form_consulta = ConsultaPetForm()
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})

def listar_consulta_id(request, id):
    consulta = consulta_pet_service.listar_consulta(id)
    return render(request, 'consultas/lista_consulta.html', {'consulta': consulta})