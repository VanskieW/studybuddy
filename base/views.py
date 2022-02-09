from django.shortcuts import render
from .models import Room

rooms = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "Javascript"},
    {"id": 3, "name": "React"},
]

def home(request):

    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render (request, 'base/home.html', context)

def room(request, pk):

    room = None
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render (request, 'base/rooms.html', context)

def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)

# Create your views here