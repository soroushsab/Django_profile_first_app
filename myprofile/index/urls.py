from django.urls import path
from index import views


urlpatterns = [
    path(r'', views.index , name= 'index'),
    path(r'dashboard/', views.dashboard , name= 'dashboard'),
    path(r'contactme/', views.contactme , name= 'contactme'),
    path(r'login/', views.login , name= 'login'),
]