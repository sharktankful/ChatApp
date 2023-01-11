import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    # connects user to the websocket and creates a group name for the chat room
    async def connect(self):
        self.roomGroupName = 'group_chat_gfg'
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()
    
    # removes user from the websocket/group
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )
    
    # Recieves text data from the websocket and sends it to others in the group chat
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        self.user_id = self.scope['user'].id
        await self.channel_layer.group_send(
            self.roomGroupName, {
                'type': 'sendMessage',
                'message': message,
                'username': username,
                'user_id': self.user_id
            }
        )
    
    # Sends text data from the user over the websocket
    async def sendMessage(self, event):
        message = event['message']
        username = event['username']
        user_id = event['user_id']
        await self.send(text_data = json.dumps({'message':message, 'username':username, 'user_id':user_id}))
                                                                    # 'username':username