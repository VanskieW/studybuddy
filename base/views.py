from django.shortcuts import render
from .models import Room
from .forms import RoomForm

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
    form = RoomForm()

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

# Create your views here