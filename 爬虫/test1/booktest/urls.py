from django.conf.urls import url
import booktest.views
urlpatterns = [
    url(r'^index/',booktest.views.index),
    #url(r'^(?P<num2>\d+)/(?P<num1>\d+)/(?P<num3>\d+)$',booktest.views.detail2),
    #url(r'(\d+)',booktest.views.detail),
    url(r'^getTest1/$',booktest.views.getTest1),
    url(r'^getTest2/$',booktest.views.getTest2),
    url(r'^getTest3/$',booktest.views.getTest3)


]
