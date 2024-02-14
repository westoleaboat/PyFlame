from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import ChatRoom

# Create your views here.
#@login_required
#def chat_room(request, room_id='default'):
#    try:
#        # retrieve
##        room_id = request.user#.
#        



@login_required
def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if not ChatRoom.objects.filter(name=room_name).exists():
            room = ChatRoom.objects.create(name=room_name, creator=request.user)
            return redirect('chat:room_detail', room_name=room_name)
        else:
            # room exists
            pass

    return render(request, 'chat/create_room.html')
    # return render(request, 'chat/room_detail.html')

@login_required
def room_detail(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    # Additional logic if needed
    return render(request, 'chat/room_detail.html', {'room': room})

@login_required
def chat_rooms(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})



# @login_required
# def chat_rooms(request):
#     """display list of chat rooms"""
#     rooms = ChatRoom.objects.all()
#     # return 
#     return render(request, 'chat/index.html', {'rooms':rooms})


# @login_required
# def create_room(request, room_name):
#     if request.method == 'POST':
#         if not ChatRoom.objects.filter(name=room_name).exists():
#             room = ChatRoom.objects.create(name=room_name, creator=request.user)
#             return redirect('room_detail', room_name=room_name)
#         else:
#             # room exists
#             pass

#     return render(request, 'room.html')


# @login_required
# def room_detail(request, room_name):
#     room = get_object_or_404(ChatRoom, name=room_name)
#     # Add additional logic here if needed
#     return render(request, 'room_detail.html', {'room': room})


# @login_required
# def create_room(request, room_id):
#     try:
#     #if request.method == 'POST':
#         #room_name = request.POST.get('room_name')
#         room_name = request.user.room_id.get(id=room_id)

#     except:
#         return HttpResponseForbidden()

#     return render(request, 'chat/room.html', {'room':room_name})
            

    #     if not ChatRoom.objects.filter(name=room_name).exists():
    #         room = ChatRoom.objects.create(name=room_name, creator=request.user)
    #         return redirect('room_detail', room_name=room_name)
    #     else:
    #         # room exists
    #         pass

    # return render(request, 'create_room.html')


