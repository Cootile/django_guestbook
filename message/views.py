from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Message
# Create your views here.

class MessageList(ListView):
    model = Message
    ordering = ['-id']
    #應用程式/資料模型_list.html
    #message/message_list.html

    #資料模型_list
class MessageRead(DetailView):
    model = Message

class MessageNew(CreateView):
    model = Message
    fields = ['user', 'receipt', 'subject', 'content']
    success_url = '/message/'