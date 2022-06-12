from calendar import c
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from home.models import Squad, ActiveSession, AvaliableQuests

# Sub functions
def proslevel(pros):
    '''Counts prosperity level'''
    if pros < 4:
        level = 1
    elif pros < 9:
        level = 2
    elif pros < 15:
        level = 3
    elif pros < 22:
        level = 4
    elif pros < 30:
        level = 5
    elif pros < 39:
        level = 6
    elif pros < 50:
        level = 7
    elif pros < 64:
        level = 8
    else:
        level = 9
    return level

def discount(rep):
    '''Counts discount'''
    if rep > 2:
        if rep < 7:
            discount = -1
        elif rep < 11:
            discount = -2
        elif rep < 15:
            discount = -3
        elif rep < 19:
            discount = -4
        else:
            discount = -5
    elif rep < -2:
        if rep > -7:
            discount = 1
        elif rep > -11:
            discount = 2
        elif rep > -15:
            discount = 3
        elif rep > -19:
            discount = 4
        else:
            discount = 5
    else:
        discount = 0
    return discount

# View functions and Ajax
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
            AvaliableQuests(squad_id = squadid, expansion=0, mission='1', finished=False, blocked=False).save()
            if ActiveSession.objects.all().exists():
                ActiveSession.objects.all().delete()
            ActiveSession(squad_id=squadid).save()
            responsecode = 200
        else:
            responsecode = 401
        return JsonResponse({'responsecode': responsecode}, status=200)


def open_menu(request, squadid):
    squaddata = Squad.objects.filter(id=int(squadid)).values_list('squad_name', 'reputation', 'prospect', 'church')[0]
    if ActiveSession.objects.all().exists():
        ActiveSession.objects.all().delete()
    ActiveSession(squad_id=squadid).save()
    level = proslevel(squaddata[2])
    return render(request, 'menu/menu.html', {
        'squadname': squaddata[0],
        'rep': squaddata[1],
        'prospect': squaddata[2],
        'church': squaddata[3],
        'prospect_level': level,
    })
# Ajax requests to add or minus rep, prospect, church
def add_rep(request, squadid):
    if request.is_ajax():
        rep = Squad.objects.filter(id=int(squadid)).values_list('reputation')[0][0]
        result = rep + 1
        if result > 20:
            result = 20
        Squad.objects.filter(id=int(squadid)).update(reputation=result)
        discount_am = discount(result)
        responsecode = 200
    else:
        responsecode = 401
    return JsonResponse({'responsecode': responsecode, 'result': result, 'disc': discount_am}, status=200)

def min_rep(request, squadid):
    if request.is_ajax():
        rep = Squad.objects.filter(id=int(squadid)).values_list('reputation')[0][0]
        result = rep - 1
        if result < -20:
            result = -20
        Squad.objects.filter(id=int(squadid)).update(reputation=result)
        discount_am = discount(result)
        responsecode = 200
    else:
        responsecode = 401
    return JsonResponse({'responsecode': responsecode, 'result': result, 'disc': discount_am}, status=200)

def add_pro(request, squadid):
    if request.is_ajax():
        pro = Squad.objects.filter(id=int(squadid)).values_list('prospect')[0][0]
        result = pro + 1
        if result > 64:
            result = 64
        Squad.objects.filter(id=int(squadid)).update(prospect=result)
        responsecode = 200
        level = proslevel(result)
    else:
        responsecode = 401
    return JsonResponse({'responsecode': responsecode, 'result': result, 'level': level}, status=200)

def min_pro(request, squadid):
    if request.is_ajax():
        pro = Squad.objects.filter(id=int(squadid)).values_list('prospect')[0][0]
        result = pro - 1
        if result < 0:
            result = 0
        Squad.objects.filter(id=int(squadid)).update(prospect=result)
        responsecode = 200
        level = proslevel(result)
    else:
        responsecode = 401
    return JsonResponse({'responsecode': responsecode, 'result': result, 'level': level}, status=200)

def add_ch(request, squadid):
    if request.is_ajax():
        church = Squad.objects.filter(id=int(squadid)).values_list('church')[0][0]
        result = church + 10
        Squad.objects.filter(id=int(squadid)).update(church=result)
        responsecode = 200
    else:
        responsecode = 401
    return JsonResponse({'responsecode': responsecode, 'result': result}, status=200)

def min_ch(request, squadid):
    if request.is_ajax():
        church = Squad.objects.filter(id=int(squadid)).values_list('church')[0][0]
        result = church - 10
        if result < 0:
            result = 0
        Squad.objects.filter(id=int(squadid)).update(church=result)
        responsecode = 200
    else:
        responsecode = 401
    return JsonResponse({'responsecode': responsecode, 'result': result}, status=200)


def gloom_map(request, squadid):
    '''Function for map view'''
    squaddata = Squad.objects.filter(id=int(squadid)).values_list('squad_name', 'reputation', 'prospect', 'church')[0]
    get_quests = AvaliableQuests.objects.filter(squad_id=squadid, expansion=0).values_list('mission')
    if ActiveSession.objects.all().exists():
        ActiveSession.objects.all().delete()
    ActiveSession(squad_id=squadid).save()
    level = proslevel(squaddata[2])
    questlist = []
    for i in get_quests:
        result = i[0]
        questlist.append(result)

    return render(request, 'map/map.html', {
        'squadname': squaddata[0],
        'rep': squaddata[1],
        'prospect': squaddata[2],
        'church': squaddata[3],
        'prospect_level': level,
        'get_quests': questlist,
    })