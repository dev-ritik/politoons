from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.alltoons, name='alltoons'),
    path('all/<asd>', views.thistoon, name='thistoon'),

]
