from django.conf.urls import url
from SearchDB.views import get_text, refreshDatabase
# from.import views 

app_name = 'SearchDB'
urlpatterns = [
    url(r'^$', get_text),
    url(r'^update/$', refreshDatabase),
]
