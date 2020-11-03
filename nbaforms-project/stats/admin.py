"""
username: nick
password: Cole1997.
"""

from django.contrib import admin
from .models import Player, Stat

admin.site.register(Player)
admin.site.register(Stat)
