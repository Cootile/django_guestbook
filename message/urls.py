from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageList.as_view(), name='msg_list'),  # message/ => 留言列表
    path('<int:pk>/', views.MessageRead.as_view(), name='msg_read'),
    path('create/', views.MessageNew.as_view(), name='msg_create'),
]