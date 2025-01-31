from django.db import models
from datetime import datetime, time

# --------------------------------
# Clase Usuario
# --------------------------------
class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('DueñoMascota', 'Dueño de Mascota'),
        ('Proveedor', 'Proveedor de Servicios'),
        ('Administrador', 'Administrador del Sistema')
    ]
    
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    tipoUsuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nombre} ({self.tipoUsuario})"

   
# --------------------------------
# Clase Mascota (composición con Usuario)
# --------------------------------
class Mascota(models.Model):
    idMascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    historialSalud = models.TextField()
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mascotas', limit_choices_to={'tipoUsuario': 'DueñoMascota'})

    class Meta:
        db_table = 'mascota'

    def __str__(self):
        return f"{self.nombre} ({self.raza})"

   


class Servicio(models.Model):
    TIPO_SERVICIO_CHOICES = [
        ('Veterinario', 'Veterinario'),
        ('Peluquería', 'Peluquería'),
        ('Paseos', 'Paseos'),
        ('Guardería', 'Guardería'),
    ]

    idServicio = models.AutoField(primary_key=True)
    tipoServicio = models.CharField(max_length=50, choices=TIPO_SERVICIO_CHOICES)
    descripcion = models.TextField()
    duracion = models.IntegerField()  # en minutos
    costo = models.FloatField()

    class Meta:
        db_table = 'servicio'

    def __str__(self):
        return f"{self.tipoServicio} - {self.descripcion}"

    


# --------------------------------
# Clase Proveedor (agregación con Servicio)
# --------------------------------
class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    horarioDisponibilidad = models.TextField()  # Se puede refinar con Horario
    servicios = models.ManyToManyField(Servicio)

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre

# --------------------------------
# Clase Cita
# --------------------------------
class Cita(models.Model):
    ESTADO_CITA_CHOICES = [
        ('Programada', 'Programada'),
        ('Cancelada', 'Cancelada'),
        ('Finalizada', 'Finalizada'),
    ]

    idCita = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CITA_CHOICES)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cita'

    def __str__(self):
        return f"Cita {self.idCita} - {self.estado}"

# --------------------------------
# Clase Notificación
# --------------------------------
class Notificacion(models.Model):
    idNotificacion = models.AutoField(primary_key=True)
    mensaje = models.TextField()
    fechaEnvio = models.DateTimeField(auto_now_add=True)
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'notificacion'

    def __str__(self):
        return f"Notificación para {self.destinatario}"

# --------------------------------
# Clase Horario
# --------------------------------
class Horario(models.Model):
    DIA_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    dia = models.CharField(max_length=10, choices=DIA_CHOICES)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()

    class Meta:
        db_table = 'horario'

    def __str__(self):
        return f"{self.dia} de {self.horaInicio} a {self.horaFin}"
