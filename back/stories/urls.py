from django.urls import path

from . import views


urlpatterns = [
    path('mystories/<int:mystory_id>/', views.MyStoryDetailView.as_view()),
    path('mystories/', views.MyStoryView.as_view()),

    path('<int:story_id>/', views.StoryDetailView.as_view()),
    path('', views.StoryView.as_view()),

    path('branches/<int:branch_id>/', views.BranchDetailView.as_view()),
    path('substories/<int:substory_id>/', views.SubstoryDetailView.as_view()),
]