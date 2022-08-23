from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCurrency.as_view(),name='currencies_list'),
    path('<int:pk>/', views.DetailCurrency.as_view(),name='each_currency'),
    path('<int:pk>/add',views.Addfavorite.as_view(),name='add_favorite'),
    path('<int:pk>/remove',views.Removefavorite.as_view(),name='remove_favorite'),
]