from django.conf.urls import url,include
from createform import views


urlpatterns = [
    url('^$',views.customform,name='customform'),
]