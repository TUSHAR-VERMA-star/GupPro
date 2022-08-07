from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name="homepage"),
    path('createSheet/', views.createSheet, name="createSheet"),
    path('ShowSheet/<int:pk>/', views.ShowSheet, name="ShowSheet"),
    path('joinSheet/', views.joinSheet, name="joinSheet"),
    path('OurSheet/', views.OurSheet, name="OurSheet"),
    path('pending/', views.pending, name="pending"),
    path('giveaccess/<int:id>', views.giveaccess, name="giveaccess"),
    path('noaccess/<int:id>', views.noaccess, name="noaccess"),
    path('addpeople/<int:id>', views.addpeople, name="addpeople"),
]
