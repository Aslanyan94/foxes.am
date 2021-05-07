from django.contrib import admin
# from .models import MadTeam, MadPlayers, MadTopScorer, MadTopAssister, MadTopRebounder, LesTeam, LesPlayers, \
#     LesTopScorer, LesTopRebounder, LesTopAssister, YoungTeam, YoungPlayers, OldTeam, OldPlayers
#
# admin.site.register(MadTeam)
# admin.site.register(MadPlayers)
# admin.site.register(MadTopScorer)
# admin.site.register(MadTopAssister)
# admin.site.register(MadTopRebounder)
#
#
# admin.site.register(LesTeam)
# admin.site.register(LesPlayers)
# admin.site.register(LesTopScorer)
# admin.site.register(LesTopRebounder)
# admin.site.register(LesTopAssister)
#
#
# admin.site.register(YoungTeam)
# admin.site.register(YoungPlayers)
#
# admin.site.register(OldTeam)
# admin.site.register(OldPlayers)

from .models import MadRoster,LesRoster

admin.site.register(MadRoster)
admin.site.register(LesRoster)
# Register your models here.
