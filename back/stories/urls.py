from django.urls import path

from . import views


urlpatterns = [
    path('mystories/', views.MyStoryView.as_view()),
]