from django.contrib import admin
from django.conf import settings
from django.urls import include, path


from students import views # noqa I needed an import for the application to work teachers

from teachers import views as tch_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', tch_views.index, name='index'),

    path('students/', include('students.urls')),

    path('teachers/', include('teachers.urls')),

    path('group/', include('group.urls')),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
