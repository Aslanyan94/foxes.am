from django.shortcuts import render
from django.http import HttpResponse
from parse.parsing import reg_list, sem_list, vb_list, wom_list
from .models import MadScheduleAndResults2021, MadScheduleAndResults2122, LesScheduleAndResults2021, \
    LesScheduleAndResults2122


#
def alg_views(request):
    if request.method == "GET":
        mad_2021_query = MadScheduleAndResults2021.objects.all()
        mad_2122_query = MadScheduleAndResults2122.objects.all()
        context = {
            "reg_list": reg_list,
            "sem_list": sem_list,
            "schedule2021": mad_2021_query,
            "schedule2122": mad_2122_query,
        }
        return render(request, "league/a_league.html", context)


def vb_arm_views(request):
    if request.method == "GET":
        context = {
            "vb_list": vb_list,
        }
        return render(request, "league/vb_arm.html", context)


def wom_views(request):
    if request.method == "GET":
        les_2021_query = LesScheduleAndResults2021.objects.all()
        les_2122_query = LesScheduleAndResults2122.objects.all()
        context = {
            "wom_list": wom_list,
            "schedule2021": les_2021_query,
            "schedule2122": les_2122_query,
        }
        return render(request, "league/women.html", context)
