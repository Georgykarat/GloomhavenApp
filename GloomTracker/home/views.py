from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from home.models import Squad, ActiveSession


def home(request, *args, **kwargs):
    if Squad.objects.all().exists():
        squads = Squad.objects.all()
    else:
        squads = None
    return render(request, 'home/home.html', {
        'squads': squads,
    })

def create_squad(request):
    if request.is_ajax():
        squadname = request.GET.get('squadname')
        squaddesc = request.GET.get('squaddesc')
        if squadname and squaddesc:
            Squad(squad_name=squadname, squad_desc=squaddesc).save()
            squadid = Squad.objects.filter(squad_name=squadname).values_list('id')[0][0]
            if ActiveSession.objects.all().exists():
                ActiveSession.objects.all().delete()
            ActiveSession(squad_id=squadid).save()
            responsecode = 200
        else:
            responsecode = 401
        return JsonResponse({'responsecode': responsecode}, status=200)


def open_menu(request, squadid):
    squaddata = Squad.objects.filter(id=int(squadid)).values_list('squad_name', 'reputation')[0]
    if ActiveSession.objects.all().exists():
        ActiveSession.objects.all().delete()
    ActiveSession(squad_id=squadid).save()
    return render(request, 'menu/menu.html', {
        'squadname': squaddata[0],
        'rep': squaddata[1],
    })
