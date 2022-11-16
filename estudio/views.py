from django.shortcuts import render
from django.http import HttpResponse

def estudio(request):
    return HttpResponse('Estudio Jurídico 👔')

def presentar(request):
    return HttpResponse(f"""
                        <h1>Estudio jurídico Villarreal</h1>
                        """)
    
def especialidad(request, rama):
    return HttpResponse(f"""
                        <h2>Derecho {rama}</h2>
                        """)
    
    

