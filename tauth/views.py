import json
from django.shortcuts import render

from django.http import HttpResponse

from .models import User


def index(request):
    return HttpResponse("User index page.")


def add_room(request):
    obj = json.loads(request.body)

    r = User.objects.update_or_create(**obj)

    return HttpResponse(r)
