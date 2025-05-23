from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

from chat_app.models import ChatRoom, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        room = data["room"]

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
                "room": room,
            },
        )

        await self.save_message(message, username, room)

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        room = event["room"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "room": room,
                }
            )
        )

    @sync_to_async
    def save_message(self, message, username, room):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room)
        message = Message(user=user, room=room, content=message)
        message.save()
