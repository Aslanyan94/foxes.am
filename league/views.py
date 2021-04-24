from django.shortcuts import render
from .models import LesTeam, LesMatches, LesPlayers
from django.http import HttpResponse
import json


def teams(request):
    if request.method == "GET":
        less_queryset = LesTeam.objects.all()
        response = []
        game = {}
        for game_query in less_queryset:
            game["team_name"] = game_query.team_name
            game["avg_point"] = game_query.avg_point
            response.append(game)
        # response = json.dumps(response)
        return HttpResponse(json.dumps({
            'status': 'ok',
            'data': response,
        }), status=200, content_type='application/json')

