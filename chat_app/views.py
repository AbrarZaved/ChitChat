from django.shortcuts import redirect, render

from chat_app.models import ChatRoom, Message


# Create your views here.
def index(request):
    rooms = ChatRoom.objects.all()
    return render(request, "index.html", {"rooms": rooms})


def chat_room(request, slug):
    chat_room = ChatRoom.objects.get(slug=slug)
    messages = Message.objects.filter(room=chat_room)[:30]
    return render(
        request, "room_details.html", {"chat_room": chat_room, "messages": messages}
    )


def create_room(request):
    if request.method == "POST":
        room_name = request.POST.get("room_name")
        room = ChatRoom.objects.create(name=room_name)
        return redirect("index")


def delete_room(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    room.delete()
    return redirect("index")
