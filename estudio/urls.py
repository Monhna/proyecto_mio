from django.urls import path

from . import views

urlpatterns = [
    path('estudio/', views.estudio),
    path('presentar/', views.presentar),
    path('especialidad/<str:rama>', views.especialidad)
]