from django.urls import path, include
from chat.consumers import ChatConsumer


websocket_patterns = [
    path('', ChatConsumer.as_asgi())
]