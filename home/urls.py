from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('projects/', views.projects, name='projects'),
    path("about/", views.about, name="about"),
    path("certificates/", views.certificates, name="certificates"),
    path("contact/", views.contact, name="contact"),
]


