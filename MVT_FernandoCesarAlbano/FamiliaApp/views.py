from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Familia

# Create your views here.

def mi_familia(reqest):
    #Definimos objeto tipo Familia
    familiar1=Familia(nombre="Alberto", parentesco="Padre", edad=78, f_nacimto="1944-06-02")
    familiar2=Familia(nombre="Susana", parentesco="Madre", edad=77, f_nacimto="1945-04-25")
    familiar3=Familia(nombre="Nicolas", parentesco="Hermano", edad=39, f_nacimto="1984-05-25")
    #Lo guardamos en la base
    familiar1.save()
    familiar2.save()
    familiar3.save()
    diccionario={"nombre_f1":familiar1.nombre, "parentesco_f1":familiar1.parentesco, "edad_f1":familiar1.edad, "f_nacimto_f1":familiar1.f_nacimto, \
                 "nombre_f2":familiar2.nombre, "parentesco_f2":familiar2.parentesco, "edad_f2":familiar2.edad, "f_nacimto_f2":familiar2.f_nacimto, \
                 "nombre_f3":familiar3.nombre, "parentesco_f3":familiar3.parentesco, "edad_f3":familiar3.edad, "f_nacimto_f3":familiar3.f_nacimto
                }
    plantilla=loader.get_template('t_familia.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
