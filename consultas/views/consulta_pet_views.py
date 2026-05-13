from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from consultas.forms.consulta_pet_form import ConsultaPetForm
from consultas.services import consulta_pet_service
from consultas.entidades.consulta_pet import ConsultaPet
from pets.services import pet_service
from django.conf import settings



@user_passes_test(lambda u: u.cargo == 1)
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

@login_required
def listar_consulta_id(request, id):
    consulta = consulta_pet_service.listar_consulta(id)
    return render(request, 'consultas/lista_consulta.html', {'consulta': consulta})

@login_required
def enviar_email_consulta(request, id):
    consulta = consulta_pet_service.listar_consulta(id)
    pet_consulta = pet_service.listar_pet_id(consulta.pet.id)
    assunto = 'Resumo da consulta do seu PET'
    html_conteudo = render_to_string('consultas/consulta_email.html', {'consulta': consulta})
    corpo_email = 'Resumo da sua consulta'
    email_remetente = settings.EMAIL_HOST_USER
    email_destino = [pet_consulta.dono.email]
    send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=html_conteudo)
    return redirect('listar_consulta_id', id)