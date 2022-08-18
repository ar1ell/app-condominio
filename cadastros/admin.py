from django.contrib import admin

from .models import Apto, Registro, Tipo, Item
# Register your models here.
admin.site.register(Apto)
admin.site.register(Registro)
admin.site.register(Tipo)
admin.site.register(Item)