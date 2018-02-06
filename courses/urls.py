from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.ListCourse.as_view(),name='List Course'),
]
