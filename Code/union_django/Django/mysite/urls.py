from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views
from calc import views as calc_views

urlpatterns = [
  url(r'^home/', learn_views.home, name='home'),
  url(r'^add/', calc_views.add, name='add'),
  url(r'^admin/', include(admin.site.urls)),
]
