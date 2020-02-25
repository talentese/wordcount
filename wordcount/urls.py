from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),

#the best here is to add the name so even if I change the URL it will be always working
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
]
