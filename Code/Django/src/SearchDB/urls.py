from django.conf.urls import url
from SearchDB.views import get_text, refreshDatabase

app_name = 'SearchDB'
urlpatterns = [
    url(r'^$', get_text), # If the user input this url, the request will be sent to get_text function in views.py
    url(r'^update/$', refreshDatabase),
]