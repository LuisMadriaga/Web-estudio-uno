from ast import Return
from multiprocessing import context
from django.shortcuts import render, HttpResponse

import CuatroRutas

# Create your views here.
def inicio(request):
    resp = request.GET.get('inicio') 
    contexto = {}
    contexto["nombre"] = "Luis Madriaga Acevedo"
    contexto["result"] = 'Nací en Santiago de Chile el 01 de enero de 1977. Estoy casado con Paula y tenemos una hija de 17 años de nombre Paz Belén. Soy egresado de enseñanza media como técnico en electrónica industrial. Mi experiencia laboral ha sido en gran parte como técnico en telecomunicaciones para la empresa Movistar. Actualmente vivo en la comuna de Santiago Centro y estoy cursando el cuarto semestre de la carrera de Analista Programador en el Centro de Formación Técnica INACAP sede Santiago Centro. Soy muy perseverante y me gusta estar constantemente aprendiendo.'

    return render(request,"CuatroRutas/inicio.html", context=contexto)
def primos(request):    
    resp = request.GET.get('primos')
    contexto = {}    
    num = 0
    x = 1
    lista = [0] * x
    todos = [0] * 25
    cont = -1
    for x in range (0,100):
        num = x 
        primo = 0
        x = 1
        while x <= num:        
            if num % x == 0:        
                primo = primo + 1                    
            x = x + 1   
        if primo == 2:            
            lista = (num)             
            cont = cont + 1
        todos[cont] = (lista)
    print(todos)
    contexto["result"] = (todos)
    return render(request,"CuatroRutas/primos.html",context=contexto)

def factorial(request):
    resp = request.GET.get('factorial')
    contexto = {}
    import random
    notacion = (random.randrange(5, 11))
    numFact = 1
    i = 0
    x = 0
    while i < notacion:
        i = i + 1    
        x = i
        numFact = 1
        while x >= 1:
            numFact = numFact * x
            x = x - 1
    contexto["result"] = notacion, 'es' , numFact

    return render(request,"CuatroRutas/factorial.html", context=contexto)


def saludo(request):
    resp = request.GET.get('saludo')
    contexto = {}
    if resp is None:
        import datetime
        x = datetime.datetime.now()
        hora = x.hour
        if hora >=0 and hora <= 12:
            contexto["result"] = "¡Buenos Días!"  
        else:
            if hora > 12 and hora <= 20:
                contexto["result"] = "¡Buenas Tardes!"
            else:
                if hora > 20 and hora <= 23:
                    contexto["result"] = "¡Buenas Noches!"       
    return render(request,"CuatroRutas/saludo.html", context=contexto)
        


