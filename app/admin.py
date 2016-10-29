from django.contrib import admin
from app.models import *


class ExemploAdmin(admin.ModelAdmin):
	list_display = []
	for field in Exemplo._meta.fields:
		list_display.append(field.name)

admin.site.register(Exemplo, ExemploAdmin)