from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('edit/<int:musician_id>/', views.edit_musician, name='edit_musician'),
    path('delete/<int:musician_id>/', views.delete_musician, name='delete_musician'),
]
