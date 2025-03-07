from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_reservation, name='create_reservation'),
    path('<int:id>/', views.reservation_detail, name='reservation_detail'),
    path('user/<int:user_id>/', views.user_reservations, name='user_reservations'),
]
