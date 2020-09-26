from django.urls import path

from . import views


app_name = 'tts'

urlpatterns = [
    path('create_voice/', views.create_voice),
]