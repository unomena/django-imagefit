from django.conf.urls import patterns, url

from imagefit import views

urlpatterns = [
    url(r'^(?P<path_name>[\w_-]*)/(?P<format>[,\w-]+)/(?P<url>.*)/?$',
        views.resize,
        name='imagefit_resize'
        ),
]
