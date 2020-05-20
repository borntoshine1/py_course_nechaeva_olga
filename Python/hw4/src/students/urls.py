from django.urls import path

from students import views

app_name = 'students'

urlpatterns = [
    path('list/', views.students, name='list'),

    path('random/', views.random_student, name='random'),

    path('generate/', views.hundred_students, name='generate'),

    path('create/', views.create_students, name='create'),

    path('edit/', views.edit_students, name='edit'),
]
