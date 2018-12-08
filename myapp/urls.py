from django.urls import path
from . import views
from .views import ListToonsView, ThisToonsView

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.alltoons, name='alltoons'),
    path('all/<toon>', views.thistoon, name='thistoon'),
    path('api/', ListToonsView.as_view(), name="toons-all"),
    path('api/<toon>', ThisToonsView.as_view(), name="toon")

]
