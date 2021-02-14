from django.shortcuts import render
from django.http import HttpResponse
from .models import Association
import os
import re
from django.urls import reverse
from . import ApiCalls

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def index(request):
    latest_question_list = Association.objects.filter(EntCategoria='Educacion')[:5]
    latest_question_list_salud = Association.objects.filter(EntCategoria='Salud')[:5]
    latest_question_list_comida = Association.objects.filter(EntCategoria='Comida')[:5]
    latest_question_list_tercera = Association.objects.filter(EntCategoria='Tercera Edad')[:5]
    latest_question_list_psicology = Association.objects.filter(EntCategoria='Psicologia')[:5]
    latest_question_list_trabajo = Association.objects.filter(EntCategoria='Trabajo')[:5]
    latest_question_list_mambiente = Association.objects.filter(EntCategoria='Medio Ambiente')[:5]
    latest_question_list_otros = Association.objects.filter(EntCategoria='Otros')[:5]
    context = {'latest_question_list': latest_question_list,
     		   'latest_question_list_salud': latest_question_list_salud,
     		   'latest_question_list_comida': latest_question_list_comida,
     		   'latest_question_list_tercera': latest_question_list_tercera,
     		   'latest_question_list_psicology': latest_question_list_psicology,
     		   'latest_question_list_trabajo': latest_question_list_trabajo,
     		   'latest_question_list_mambiente': latest_question_list_mambiente,
     		   'latest_question_list_otros': latest_question_list_otros}
    print(context)
    return render(request, 'index.html', context)
 

 
def results(request):
    #print("gh46jh3")
    #print("Llego1")

    param1 = request.POST.get("input-text")
    #(param1)
    #print ('flipa con este parametro')
    #print(param1);
    tag = ApiCalls.CallApis(param1)
    latest_question_list = Association.objects.filter(EntCategoria=tag)[:5]
    context = {'latest_question_list': latest_question_list}

    # if a is not None:
    # send_mail_Alert()
    return render(request, 'results.html', context)