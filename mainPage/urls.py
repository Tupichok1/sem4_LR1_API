from django.urls import path
from . import views

urlpatterns = [
    path('home', views.AllAttacks.as_view(), name = 'homePage'),
    path('createNote', views.CreateNote.as_view(), name = 'createNote'),
    path('updateNote/<int:pk>', views.UpdateDeleteNote.as_view(), name = 'updateNote'),
]