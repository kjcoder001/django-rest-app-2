""" FROM STACKOVERFLOW-->I finally understand how the .create() and .update() work in Serializer (especially ModelSerializer) and how they
 are connected to Viewsets (especially ModelViewSet). I just want clarify the concept more clearly if someone
 comes to this question.

Basically, the 4 methods CRUD in ModelViewSet: .create(), .retrieve(),
.update(), and .destroy() will handle the calls from HTTP verbs. By default, the .create() and .update() from
 ModelViewSet will call the .create() and .update() from ModelSerializer by calling the .save() method from the
 BaseSerializer class.

The save() method will then determine whether it will call .create() or .update() in ModelSerializer by
determining whether the object self.instance exists or not."""

from rest_framework import serializers
from . import models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','url')
        model=models.Course


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','course','name','email','comment','rating','created_at')
        model=models.Review
        extra_kwargs={'email':{'write_only':True}}
        # the email of people or users shoudn't be displayed on the site
        # just like that .Hence its only write_only and cannot be read.
