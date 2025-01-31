from mascotas.models import Mascota, Servicio
from django.shortcuts import get_object_or_404

# Métodos
def iniciarSesion(self, email, password):
    """Verifica si el email y contraseña son correctos."""
    if self.email == email and self.contraseña == password:
        return "Sesión iniciada correctamente."
    else:
         return "Credenciales incorrectas."

def cerrarSesion(self):
    """Lógica para cerrar sesión."""
    return "Sesión cerrada."

# Métodos
def registrarMascota(self):
    """Registra una nueva mascota."""
    return f"Mascota {self.nombre} registrada correctamente."

def actualizarInformacion(self, nombre=None, raza=None, edad=None, historialSalud=None):
    """Actualiza la información de la mascota."""
    if nombre: self.nombre = nombre
    if raza: self.raza = raza
    if edad: self.edad = edad
    if historialSalud: self.historialSalud = historialSalud
    self.save()
    return "Información actualizada."

def consultarHistorial(self):
    """Consulta el historial de salud de la mascota."""
    return f"Historial de {self.nombre}: {self.historialSalud}"

# Métodos
def listarServicios():
    """Lista todos los servicios disponibles."""
    return Servicio.objects.all()

def buscarServicio(tipo, ubicacion):
    """Busca servicios por tipo y ubicación (simplificado, sin ubicación)."""
    return Servicio.objects.filter(tipoServicio=tipo)

# Métodos
def registrarProveedor(self):
    """Registra un nuevo proveedor."""
    return "Proveedor {self.nombre} registrado correctamente."

def actualizarDisponibilidad(self, nuevo_horario):
    """Actualiza la disponibilidad del proveedor."""
    self.horarioDisponibilidad = nuevo_horario
    self.save()
    return "Disponibilidad actualizada."

def consultarAgenda(self):
    """Consulta la agenda del proveedor."""
    return f"Agenda de {self.nombre}: {self.horarioDisponibilidad}"

# Métodos
def programarCita(self):
    """Programa una cita."""
    return f"Cita programada para {self.fecha} a las {self.hora}."

def modificarCita(self, nueva_fecha, nueva_hora):
    """Modifica una cita."""
    self.fecha = nueva_fecha
    self.hora = nueva_hora
    self.save()
    return "Cita modificada."

def cancelarCita(self):
    """Cancela una cita."""
    self.estado = 'Cancelada'
    self.save()
    return "Cita cancelada."

# Métodos
def enviarNotificacion(self):
    """Envia una notificación."""
    return f"Notificación enviada a {self.destinatario.nombre}."

def programarRecordatorio(self, fecha):
    """Programa un recordatorio."""
    return f"Recordatorio programado para {fecha}."