from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import ChatSerializer
from .models import Chat
# Create your views here.

class ChatView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatList(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatRetrieve(generics.RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatUpdate(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    
class ChatDelete(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    