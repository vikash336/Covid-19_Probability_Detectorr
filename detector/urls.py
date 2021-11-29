from django.conf.urls import url

from detector import views

urlpatterns=[
    url('vik',views.vik),
    url('result',views.result),

]
