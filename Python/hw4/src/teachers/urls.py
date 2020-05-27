from django.conf import settings # noqa imported but unused
from django.urls import path


from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.teachers, name='list'),

    path('generate/', views.generate, name='generate'),

    path('create/', views.create_teacher, name='create'),

    path('edit/<int:pk>/', views.edit_teacher, name='edit'),

    path('delete/<int:pk>/', views.delete_teacher, name='delete'),
]
