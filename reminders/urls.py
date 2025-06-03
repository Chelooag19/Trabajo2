from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_reminder, name='create_reminder'),
    path('update/<uuid:id>/', views.update_reminder, name='update_reminder'),
    path('delete/<uuid:id>/', views.delete_reminder, name='delete_reminder'),
]
