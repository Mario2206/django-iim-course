import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class MessengerConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "all",
            self.channel_name
        )
        return await self.accept()
    
    async def disconnect(self, code):
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
       

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send("all", {
            'type': 'send_message',
            'message': message
        })
    
    async def send_message(self, res):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(res))