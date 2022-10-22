from asgiref.sync import sync_to_async
from django.shortcuts import redirect, render, HttpResponse
# importing loading from django template


from .models import Messages

# An index view that lets you type the name of a chat room to join.
def index(request):
    return render(request, 'justchat/index.html', {})

# A room view that lets you see messages posted in a particular chat room.
# The room view will use a WebSocket to communicate with the Django server
#  and listen for any messages that are posted.
def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('/chat/')

    message = Messages.objects.filter(room_name=room_name)
    return render(request, 'justchat/room.html', context={
        'room_name': room_name, 'user': request.user.username, 'message': message
    })


@sync_to_async
def create_chat(data):
    if "username" not in data.keys():
        data["username"] = "undefined"

    if "room_name" not in data.keys():
        data["room_name"] = "lobby"

    Messages.objects.create(**data)
