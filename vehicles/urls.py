from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('add/', views.add_vehicle, name='add'),

    path('list/', views.vehicle_list, name='vehicle_list'),

    path('detail/<int:id>/', views.vehicle_detail,
         name='detail'),

    path('update/<int:id>/', views.update_vehicle,
         name='update'),

    path('delete/<int:id>/', views.delete_vehicle,
         name='delete'),
]