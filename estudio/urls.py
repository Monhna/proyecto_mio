from django.urls import path

from . import views

urlpatterns = [
    path('estudio/', views.estudio),
    path('estudio/presentar/', views.presentar),
    path('estudio/buscar_especialidad/<str:rama>', views.buscar_especialidad),
    path('admin/ver_expedientes/<int:anio>/<int:mes>', views.ver_expedientes),
]