from rest_framework import generics # replaces API view and other classes from previous commits
from django.shortcuts import get_object_or_404
from . import serializers
from . import models
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.response import Response


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

class ListCreateReview(generics.ListCreateAPIView):
    """Fetches reviews from the models(db) and lists them for a particular course . Option to create a new review also."""
    # url pattern is-->e.g api/v1/courses/1/reviews/ --> list all reviews for this course
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer

    def get_queryset(self):

        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
    # difference between course_id and course.id-->course_id just does a database lookup .It doesn't go the db and
    # fetches the data.
    # course_pk has been referenced here from the urls.

    def perform_create(self,serializer):
        """ This method is run right when the object is being created by the view. """

        #This method prevents a user from being able to give a different pk whilst they are submitting a review.
        course=get_object_or_404(models.Course,pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    """ particular review detail for a particular course ."""
    # the url pattern ,e.g is api/v1/courses/1(course_id)/reviews/1(pk) --> first review from the first course
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer

    # this method is used to get a particular review from a particular course.

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            course_id=self.kwargs.get('course_pk'),
            pk=self.kwargs.get('pk')
        )

# VIEWSETS BEGIN HERE FOR VERSION 2 OF THE api
# The url-->api/v2/courses/1/ would work just fine but api/v2/courses/1/reviews won't work because rest_framework viewsets
# only generate typical crud views  from one model.So you can do crud operations only for one single model.

# To run that url there is a provision of creating ad-hoc methods in a viewset by importing a decorator

class CourseViewSet(viewsets.ModelViewSet):
    queryset=models.Course.objects.all()
    serializer_class=serializers.CourseSerializer

    @detail_route(methods=['get'])

    def reviews(self,request,pk=None): # this method basically lists all the reviews for the course
        course=self.get_object() # to ascertain the course which is under consideration

        serializer=serializers.ReviewSerializer(
        course.reviews.all(),many=True)
        # wtf is course.reviews.all()?!
        #ans found from forums-->The Review model class has a Foreign key course with the related name 'reviews'. So
        #'reviews' is used for the relation from Course back to Review.)

        return Response(serializer.data)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer
