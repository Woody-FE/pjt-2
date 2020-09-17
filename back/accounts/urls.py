from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('<int:user_id>/', views.UserDetailView.as_view()),
    path('<int:user_id>/child/image/', views.UserImageUpdateView.as_view()),
    path('<int:user_id>/family/', views.UserFamilyView.as_view()),
    path('<int:user_id>/family/<int:family_id>/', views.UserFamilyDetailView.as_view()),
]