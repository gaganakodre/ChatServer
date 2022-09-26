# chat/views.py
from datetime import timezone
import json

from asgiref.sync import sync_to_async
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
# importing loading from django template
from django.template import loader

from . models import Messages


def index(request):
    return render(request, 'justchat/index.html', {})

def room(request, room_name):
    user=request.user
    print(user)
    message=Messages.objects.filter(room_name=room_name)
    print(message)
    return render(request, 'justchat/room.html', context={
        'room_name': room_name,'user':user.username,'message':message
    })

@sync_to_async
def create_chat(data):
    if "username" not in data.keys():
        data["username"]="undefined"

    if "room_name" not in data.keys():
        data["room_name"]="lobby"

    Messages.objects.create(**data)
        # room_name = .GET["roomname"]
        # username = request.GET["username"]
        # message = request.GET["message"]
        # msg = Messages(room_name=room_name,username=username,message=message,
        #                 created_at=timezone.now())
        # msg.save()
        # return redirect('create_chat')
    # return render(request, 'justchat/room.html', {
    # 'room_name': room_name,'username':username
    # })
