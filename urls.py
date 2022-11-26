from django.urls import path
from . import views

urlpatterns = [
    path('', views.table),
    path('update/<str:id>/', views.update, name='update')
]