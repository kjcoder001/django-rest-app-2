from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.ListCreateCourse.as_view(),name='List Create Course'),
]
