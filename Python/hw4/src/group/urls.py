from django.conf import settings
from django.urls import path

from group import views

app_name = 'group'

urlpatterns = [
    path('create/', views.create_group, name='create'),
]
