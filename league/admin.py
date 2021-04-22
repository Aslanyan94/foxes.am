from django.contrib import admin
from .models import  *

admin.site.register(MadTeam)
admin.site.register(MadPlayers)

admin.site.register(LesTeam)
admin.site.register(LesPlayers)

admin.site.register(YoungTeam)
admin.site.register(YoungPlayers)

admin.site.register(OldTeam)
admin.site.register(OldPlayers)

admin.site.register(MadMatches)
admin.site.register(LesMatches)
admin.site.register(YoungMatches)
admin.site.register(OldMatches)
# Register your models here.
