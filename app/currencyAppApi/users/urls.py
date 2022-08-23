from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.Registeration.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('watchlist/', views.Watchlist.as_view(),name='watch_list'),
]