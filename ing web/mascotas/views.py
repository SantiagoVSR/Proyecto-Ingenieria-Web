from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario

# Vista para la página de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Usuario.objects.filter(email=email, contraseña=password).first()

        if user:
            # Redirigir según el tipo de usuario
            if user.tipoUsuario == 'DueñoMascota':
                return redirect('dueno_home')
            elif user.tipoUsuario == 'Proveedor':
                return redirect('proveedor_home')
            elif user.tipoUsuario == 'Administrador':
                return redirect('administrador_home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas.'})

    return render(request, 'login.html')

def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        tipoUsuario = request.POST['tipoUsuario']

        # Crear un nuevo usuario
        if tipoUsuario in ['DueñoMascota', 'Proveedor']:
            Usuario.objects.create(
                nombre=nombre,
                email=email,
                contraseña=contraseña,
                tipoUsuario=tipoUsuario
            )
            return redirect('login')  # Redirigir al login después del registro

    return render(request, 'registro.html')

# Vista para el dueño de mascota
def dueno_home(request):
    return render(request, 'dueno_home.html')

# Vista para el proveedor
def proveedor_home(request):
    return render(request, 'proveedor_home.html')

# Vista para el administrador
def administrador_home(request):
    return render(request, 'administrador_home.html')


