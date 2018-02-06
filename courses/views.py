from rest_framework import generics # replaces API view and other classes from previous commits

from . import serializers
from . import models


class ListCreateCourse(generics.ListCreateAPIView):
    """Concrete view for listing a queryset or creating a model instance """

    # 2 attributes:-
    queryset=models.Course.objects.all()
    # queryset it will use to find the objects that it needs to listing
    serializer_class=serializers.CourseSerializer
    # specifies the serializer it should use in order to serialize the queryset that it receives
