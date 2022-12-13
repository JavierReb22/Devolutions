from django.contrib import admin
from . import models as m

# Register your models here.
admin.site.register(m.Cliente)
admin.site.register(m.Producto)
admin.site.register(m.Devolucion)

