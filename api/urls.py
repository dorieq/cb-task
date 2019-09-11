from django.urls import path
from api import views

urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.review_detail),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
]