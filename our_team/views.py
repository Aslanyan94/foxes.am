from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import MadTeam, MadPlayers, MadTopRebounder, MadTopScorer, MadTopAssister, LesTeam, LesPlayers, \
    LesTopAssister, LesTopRebounder, LesTopScorer, YoungTeam, YoungPlayers, OldTeam, OldPlayers


def mad_views(request):
    if request.method == "GET":

        # Mad Team
        mad_team_queryset = MadTeam.objects.all()
        response_team = []
        team = {}
        for game_query in mad_team_queryset:
            team["team_name"] = game_query.team_name
            team["games_played"] = game_query.games_played
            team["pts"] = game_query.pts
            team["avg_point"] = game_query.avg_point
            response_team.append(team)

        #     Mad Players
        mad_players_queryset = MadPlayers.objects.all()
        response_players = []
        players = {}
        for game_query in mad_players_queryset:
            players["player_fullname"] = game_query.player_fullname
            players["sh_number"] = game_query.sh_number
            players["g_played"] = game_query.g_played
            players["position"] = game_query.position
            players["height"] = game_query.height
            players["b_date"] = game_query.b_date
            players["pts"] = game_query.pts
            players["avg_point"] = game_query.avg_point
            response_players.append(players)

        #     Mad TopScorer
        mad_scorer_queryset = MadTopScorer.objects.all()
        response_scorer = []
        scorer = {}
        for score_query in mad_scorer_queryset:
            scorer["player"] = score_query.player.player_fullname
            scorer["point"] = score_query.point
            response_scorer.append(scorer)

        #     Mad TopRebounder
        mad_rebounder_queryset = MadTopRebounder.objects.all()
        response_rebounder = []
        rebounder = {}
        for game_query in mad_rebounder_queryset:
            rebounder["player"] = game_query.player.player_fullname
            rebounder["point"] = game_query.point
            response_rebounder.append(rebounder)

        #     Mad Top Assister
        mad_assister_queryset = MadTopAssister.objects.all()
        response_assister = []
        assister = {}
        for game_query in mad_assister_queryset:
            assister["player"] = game_query.player.player_fullname
            assister["point"] = game_query.point
            response_assister.append(assister)
        return HttpResponse(json.dumps({
            'status': 'ok',
            'data_team': response_team,
            'data_players': response_players,
            'data_scorer': response_scorer,
            'data_rebounder': response_rebounder,
            'data_assister': response_assister,
        }), status=200, content_type='application/json')


def les_views(request):
    if request.method == "GET":

        # Les Team
        les_team_queryset = LesTeam.objects.all()
        response_team = []
        team = {}
        for game_query in les_team_queryset:
            team["team_name"] = game_query.team_name
            team["games_played"] = game_query.games_played
            team["pts"] = game_query.pts
            team["avg_point"] = game_query.avg_point
            response_team.append(team)

        #    Les Players
        les_players_queryset = LesPlayers.objects.all()
        response_players = []
        players = {}
        for game_query in les_players_queryset:
            players["player_fullname"] = game_query.player_fullname
            players["sh_number"] = game_query.sh_number
            players["g_played"] = game_query.g_played
            players["position"] = game_query.position
            players["height"] = game_query.height
            players["b_date"] = game_query.b_date
            players["pts"] = game_query.pts
            players["avg_point"] = game_query.avg_point
            response_players.append(players)

        #     Les TopScorer
        les_scorer_queryset = LesTopScorer.objects.all()
        response_scorer = []
        scorer = {}
        for score_query in les_scorer_queryset:
            scorer["player"] = score_query.player.player_fullname
            scorer["point"] = score_query.point
            response_scorer.append(scorer)

        #    Les TopRebounder
        les_rebounder_queryset = LesTopRebounder.objects.all()
        response_rebounder = []
        rebounder = {}
        for game_query in les_rebounder_queryset:
            rebounder["player"] = game_query.player.player_fullname
            rebounder["point"] = game_query.point
            response_rebounder.append(rebounder)

        #     Les Top Assister
        les_assister_queryset = LesTopAssister.objects.all()
        response_assister = []
        assister = {}
        for game_query in les_assister_queryset:
            assister["player"] = game_query.player.player_fullname
            assister["point"] = game_query.point
            response_assister.append(assister)
        return HttpResponse(json.dumps({
            'status': 'ok',
            'data_team': response_team,
            'data_players': response_players,
            'data_scorer': response_scorer,
            'data_rebounder': response_rebounder,
            'data_assister': response_assister,
        }), status=200, content_type='application/json')


def young_views(request):
    if request.method == "GET":

        # Mad Team
        young_team_queryset = YoungTeam.objects.all()
        response_team = []
        team = {}
        for game_query in young_team_queryset:
            team["team_name"] = game_query.team_name
            team["games_played"] = game_query.games_played
            team["pts"] = game_query.pts
            team["avg_point"] = game_query.avg_point
            response_team.append(team)

        #     Mad Players
        young_players_queryset = YoungPlayers.objects.all()
        response_players = []
        players = {}
        for game_query in young_players_queryset:
            players["player_fullname"] = game_query.player_fullname
            players["sh_number"] = game_query.sh_number
            players["g_played"] = game_query.g_played
            players["position"] = game_query.position
            players["height"] = game_query.height
            players["b_date"] = game_query.b_date
            players["pts"] = game_query.pts
            players["avg_point"] = game_query.avg_point
            response_players.append(players)

        return HttpResponse(json.dumps({
            'status': 'ok',
            'data_team': response_team,
            'data_players': response_players,
        }), status=200, content_type='application/json')

def old_views(request):
    if request.method == "GET":

        # Old Team
        old_team_queryset = OldTeam.objects.all()
        response_team = []
        team = {}
        for game_query in old_team_queryset:
            team["team_name"] = game_query.team_name
            team["games_played"] = game_query.games_played
            team["pts"] = game_query.pts
            team["avg_point"] = game_query.avg_point
            response_team.append(team)

        #     Old Players
        old_players_queryset = OldPlayers.objects.all()
        response_players = []
        players = {}
        for game_query in old_players_queryset:
            players["player_fullname"] = game_query.player_fullname
            players["sh_number"] = game_query.sh_number
            players["g_played"] = game_query.g_played
            players["position"] = game_query.position
            players["height"] = game_query.height
            players["b_date"] = game_query.b_date
            players["pts"] = game_query.pts
            players["avg_point"] = game_query.avg_point
            response_players.append(players)

        return HttpResponse(json.dumps({
            'status': 'ok',
            'data_team': response_team,
            'data_players': response_players,
        }), status=200, content_type='application/json')

# Create your views here.
