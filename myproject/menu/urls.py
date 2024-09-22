from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:named_url>/', views.dynamic_page, name='dynamic_page'),
]