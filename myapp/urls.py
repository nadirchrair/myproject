from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
    path('groupebactirie/<int:id>/', views.groupebactirie, name='groupebactirie'),
    path('group/<int:group_id>/bacteries/', views.bactirie, name='bactirie'),
    path('predection/', views.predection, name='predection'),



]