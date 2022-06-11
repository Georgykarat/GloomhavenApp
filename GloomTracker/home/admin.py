from django.contrib import admin
from home.models import Squad
# Register your models here.

class SquadAdmin(admin.ModelAdmin):
    list_display = ['id', 'squad_name', 'squad_start', 'squad_last','reputation', 'prospect', 'church']
    search_fields = ['squad_name']

admin.site.register(Squad, SquadAdmin)