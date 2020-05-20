from django.conf import settings
from django.urls import path


from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('teachers/', views.teachers, name='list'),

    path('create/', views.create_teacher, name='create'),
]
