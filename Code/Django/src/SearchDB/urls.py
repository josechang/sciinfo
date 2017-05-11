from django.conf.urls import url
from . import views

app_name = 'SearchDB'
urlpatterns = [
    url(r'^$', views.get_text),
    url(r'^yourText/$', views.show_text),
]
