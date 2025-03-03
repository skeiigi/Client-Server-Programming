from django.urls import path
from . import views

urlpatterns = [
    path('my_form/', views.my_form_view, name='my_form'),
    path('', views.main_view, name="main_view")
]