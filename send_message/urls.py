from django.urls import path
from .views import SendMessage, SendChannel

urlpatterns = [
    path("send-message/", SendMessage.as_view(), name="send_message"),
    path("send-channel/", SendChannel.as_view(), name="send_channel"),
]
