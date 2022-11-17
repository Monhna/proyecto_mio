from django.shortcuts import render
from django.http import HttpResponse

def estudio(request):
    return HttpResponse('Estudio Jurídico 👔')

def presentar(request):
    return HttpResponse(f"""
                        <h1>Estudio jurídico Villarreal</h1>
                        """)
    
def buscar_especialidad(request, rama='laboral'):
    return HttpResponse(f"""
                        <h2>Derecho {rama}</h2>
                        """)

def ver_expedientes(request, anio, mes):
    return HttpResponse(f"""
        <h1>Expedientes del {mes}/{anio}</h1>
        <p>Listado de expedientes por fecha</p> 
                        """)
    
    

