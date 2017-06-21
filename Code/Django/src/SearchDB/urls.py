from django.conf.urls import url
from SearchDB.views import get_text, refreshDatabase
# from.import views 

app_name = 'SearchDB'
urlpatterns = [
    url(r'^$', get_text), # If the user input this url, the request will be     sent to get_text function in views.py
    url(r'^update/$', refreshDatabase),
    url(r '^test/$', chart, name = 'demo'),
]
