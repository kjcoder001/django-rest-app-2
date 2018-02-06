from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.ListCreateCourse.as_view(),name='List Create Course'),
    url(r'(?P<pk>\d+)/$',views.RetrieveUpdateDestroyCourse.as_view(),name='Course Details'),
    # the RetrieveUpdateDestroyAPIView expect a key in the url that's named pk
]
