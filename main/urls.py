from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.LandingPageView, name='landing'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('add_event/', views.add_event, name='add_event'),
    path('events/', views.event_list, name='event_list'),  # URL za listu događaja
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),  # URL za uređivanje događaja
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),  # URL za brisanje događaja
    path('pretraga_eventova/', views.pretrazi_eventove, name='pretrazi_eventove'),


]