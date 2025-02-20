from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('section_one/', views.section_one, name='section_one'),
    path('section_two/', views.section_two, name='section_two'),
]
