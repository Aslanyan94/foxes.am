from django.shortcuts import render
from django.http import HttpResponse
# from .models import ALeagueRegular,ALeagueSemifinal,WomenChampionship
import json

#
# def algreg_views(request):
#     if request.method == "GET":
#         a_reg_queryset = ALeagueRegular.objects.all()
#         response1 = []
#         league = {}
#         for team_query in a_reg_queryset:
#             league["team"] = team_query.team.team_name
#             league["win"] = team_query.win
#             league["lose"] = team_query.lose
#             league["point"] = team_query.point
#             response1.append(league)
#
#         a_sem_queryset = ALeagueSemifinal.objects.all()
#         response2 = []
#         league2 = {}
#         for team_query in a_sem_queryset:
#             league2["team"] = team_query.team.team_name
#             league2["win"] = team_query.win
#             league2["lose"] = team_query.lose
#             league2["point"] = team_query.point
#             response2.append(league2)
#         return HttpResponse(json.dumps({
#             'status': 'ok',
#             "data_regular": response1,
#             "data_semifinal": response2,
#         }), status=200, content_type='application/json')
#
#
#
# def women_views(request):
#     if request.method == "GET":
#         wom_queryset = WomenChampionship.objects.all()
#         response_wom = []
#         league = {}
#         for team_query in wom_queryset:
#             league["team"] = team_query.team.team_name
#             league["win"] = team_query.win
#             league["lose"] = team_query.lose
#             league["point"] = team_query.point
#             response_wom.append(league)
#
#         return HttpResponse(json.dumps({
#             'status': 'ok',
#             "data_women": response_wom,
#         }), status=200, content_type='application/json')