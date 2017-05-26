from django.conf.urls import url
from SearchDB.views import get_text

app_name = 'SearchDB'
urlpatterns = [
    url(r'^search/$', get_text),
#    url(r'^yourText/$', views.show_text),
]
