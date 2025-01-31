from django.urls import path
from mascotas import views
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.login_view, name='login'),  # Página de inicio de sesión
    path('registro/', views.registro_view, name='registro'),  # Página de registro
    path('dueno/', views.dueno_home, name='dueno_home'),  # Página del dueño
    path('proveedor/', views.proveedor_home, name='proveedor_home'),  # Página del proveedor
    path('administrador/', views.administrador_home, name='administrador_home'),  # Página del administrador
]
