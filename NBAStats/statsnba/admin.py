from django.contrib import admin

from .models import Player

"""
Admin Login Info
    http://localhost:8000/admin/
        Username: nicolasthreatt
        Password: CavsHeatLakers23
"""

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'jersey_num', 'ppg', 'fg_p', 'tp_p', 'reb', 'ast']