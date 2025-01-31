from django.contrib import admin
from .models import Usuario, Mascota, Servicio, Proveedor, Cita, Notificacion

# Registra los modelos para el panel de administración
admin.site.register(Usuario)
admin.site.register(Mascota)
admin.site.register(Servicio)
admin.site.register(Proveedor)
admin.site.register(Cita)
admin.site.register(Notificacion)
