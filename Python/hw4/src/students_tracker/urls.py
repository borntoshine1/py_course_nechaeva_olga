from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from group import views as group_views

from students import views

from teachers import views as teacher_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('students/', include('students.urls')),

    path('teachers/', include('teachers.urls')),

    path('create_group/', include('group.urls')),
    
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
