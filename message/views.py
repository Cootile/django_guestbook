from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MessageList(ListView):
    model = Message
    ordering = ['-created']
    #應用程式/資料模型_list.html
    #message/message_list.html

    #資料模型_list
class MessageRead(DetailView):
    model = Message

class MessageNew(CreateView):
    model = Message
    fields = ['user', 'receipt', 'subject', 'content']
    success_url = reverse_lazy('msg_list')

class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')