from django.urls import path

from . import views


urlpatterns = [
    path('mycharacters/<int:mycharacter_id>/', views.MyCharacterDetailView.as_view()),

    path('mystories/<int:mystory_id>/substories/<int:substory_id>/', views.SubstoryDetailView.as_view()),
    path('mystories/<int:mystory_id>/mycharacter/', views.MyCharacterView.as_view()),
    path('mystories/<int:mystory_id>/mysubstories/<int:mysubstory_id>/', views.MySubStoryDetailView.as_view()),
    path('mystories/<int:mystory_id>/', views.MyStoryDetailView.as_view()),
    path('mystories/', views.MyStoryView.as_view()),

    path('branches/<int:branch_id>/', views.BranchDetailView.as_view()),

    path('<int:story_id>/substories/', views.SubStoryListView.as_view()),
    path('<int:story_id>/', views.StoryDetailView.as_view()),

    path('', views.StoryView.as_view()),
]