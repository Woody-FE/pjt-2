from django.urls import path

from . import views


app_name = 'tts'

urlpatterns = [
    path('voice/story/<int:story_id>/user/<int:user_id>/', views.create_voice),
]