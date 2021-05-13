from django.shortcuts import render
from django.http import HttpResponse
from .models import MadRoster, LesRoster
from parse.parsing import mad_pl, mad_top, mad_last_list, les_pl, les_top, les_last_list


def mad_views(request):
    if request.method == "GET":
        mad_roster_query = MadRoster.objects.all()
        # mad_roster = []
        # pl = {}
        # for pl_query in mad_roster_query:
        #     pl["pl_name"] = pl_query.pl_name
        #     pl["position"] = pl_query.position
        #     pl["height"] = pl_query.height
        #     pl["b_date"] = pl_query.b_date
        #     mad_roster.append(pl)
        context = {
            "mad_pl": mad_pl,
            "mad_top": mad_top,
            "mad_last": mad_last_list,
            # "mad_roster": mad_roster,
            "mad_roster_query": mad_roster_query,
        }
        return render(request, "our_teams/mad.html", context)


def les_views(request):
    if request.method == "GET":
        les_roster_query = LesRoster.objects.all()
        # les_roster = []
        # pl = {}
        # for pl_query in les_roster_query:
        #     pl["pl_name"] = pl_query.pl_name
        #     pl["position"] = pl_query.position
        #     pl["height"] = pl_query.height
        #     pl["b_date"] = pl_query.b_date
        #     les_roster.append(pl)
        context = {
            "mad_pl": les_pl,
            "mad_top": les_top,
            "mad_last": les_last_list,
            # "les_roster": les_roster,
            "les_roster_query": les_roster_query,
        }
        return render(request, "our_teams/les.html", context)
