from django.urls import path
from .views import ChatView, ChatList, ChatRetrieve, ChatDelete, ChatUpdate

urlpatterns = [
    path('', ChatView.as_view()),
    path('create/', ChatList.as_view()),
    path('detail/<int:pk>/', ChatRetrieve.as_view()),
    path('update/<int:pk>/', ChatUpdate.as_view()),
    path('delete/<int:pk>/', ChatDelete.as_view()),
]