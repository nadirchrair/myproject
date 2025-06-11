from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
    path('groupebactirie/<int:id>/', views.groupebactirie, name='groupebactirie'),
    path('group/<int:group_id>/bacteries/', views.bactirie, name='bactirie'),
    path('predection/', views.predection, name='predection'),
    path('predection/Entérobactéries/', views.predectionEntérobactéries, name='predectionEntérobactéries'),
    path('predection/stash/', views.predectionstash, name='predectionstash'),
    path('predection/Pseudo-Aeromonas/', views.predectionPseudo_Aeromonas, name='predectionPseudo_Aeromonas'),
 path('predection/Enterococcus/', views.predectionEnterococcus, name='predectionEnterococcus'),

 path('predection/Streptococcus/', views.predectionStreptococcus, name='predectionStreptococcus'),
  path('predection/Bacillus/', views.predectionBacillus, name='predectionBacillus'),

    path('contact/', views.contact, name='contact'),




]