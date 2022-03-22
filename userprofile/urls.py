from django.urls import path
from . import views

urlpatterns = [
    path('userprofile/', views.UserProfileList.as_view(), name='userprofile-list'),
    path('userprofile/<int:pk>/', views.UserProfileDetail.as_view(), name='userprofile-detail'),
]