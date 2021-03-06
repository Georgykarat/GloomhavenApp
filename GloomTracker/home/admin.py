from django.contrib import admin
from home.models import Squad, ActiveSession, AvaliableQuests
# Register your models here.

class SquadAdmin(admin.ModelAdmin):
    list_display = ['id', 'squad_name', 'squad_desc', 'squad_start', 'squad_last','reputation', 'prospect', 'church']
    search_fields = ['squad_name']


class ActiveSessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'squad_id']


class AvaliableQuestsAdmin(admin.ModelAdmin):
    list_display = ['squad_id', 'expansion', 'mission', 'finished', 'blocked']
    search_fields = ['squad_id']

admin.site.register(Squad, SquadAdmin)
admin.site.register(ActiveSession, ActiveSessionAdmin)
admin.site.register(AvaliableQuests, AvaliableQuestsAdmin)