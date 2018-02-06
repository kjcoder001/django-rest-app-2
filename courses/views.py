from rest_framework import generics # replaces API view and other classes from previous commits

from . import serializers
from . import models

# This class takes care of listing and creating new courses
class ListCreateCourse(generics.ListCreateAPIView):
    """Concrete view for listing a queryset or creating a model instance """

    # 2 attributes:-
    queryset=models.Course.objects.all()
    # queryset it will use to find the objects that it needs to listing
    serializer_class=serializers.CourseSerializer
    # specifies the serializer it should use in order to serialize the queryset that it receives

#This class takes care of retrieving,updating and deleting an entry from the database
class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    """ Concrete view for retrieving,updating and deleting a model instance"""
    queryset=models.Course.objects.all()
    # uses the query set to go find the data/entry that you asked for,e.g the primary-key you asked for
    serializer_class=serializers.CourseSerializer
      
