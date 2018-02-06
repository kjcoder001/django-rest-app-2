from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models

class ListCourse(APIView):

    def get(self,request,format=None):
        courses=models.Course.objects.all()# list of all objects
        serializer=serializers.CourseSerializer(courses,many=True)# many lets the serializer know that multiple courses
        # are being passed to serialize
        # Serialization process is taking place here where text-string gets converted to json format
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=serializers.CourseSerializer(data=request.data)
        # entry is made in json format ; deserialization takes place here.json format gets coverted to
        #native datatypes

        serializer.is_valid(raise_exception=True)
        # .is_valid() method can be used only when it has a data keyword argument in it.It simply validates the
        # entries and continues if everything's alright else raises an exception

        serializer.save()
        #Saves the entry to our Database.
        # Updates the serializer in memory,i.e as soon as we hit save() ,the serializer class gets assigned
        # an id , created_at etc.So now serializer.data(a dictionary)has all the attributes to display them in a view.
        return Response(serializer.data,status=status.HTTP_201_CREATED)
