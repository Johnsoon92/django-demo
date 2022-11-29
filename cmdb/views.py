import json
from django.shortcuts import render

from django.http import HttpResponse

from cmdb.models import MrRoomTb



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_room(request):
    obj=json.loads(request.body)

    r = MrRoomTb.objects.update_or_create(**obj)

    return HttpResponse(r)
