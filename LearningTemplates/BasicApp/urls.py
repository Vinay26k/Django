from django.conf.urls import url
from BasicApp import views

# for template tagging
app_name = 'BasicApp'
urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]
