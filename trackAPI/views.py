from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Workout
from .serializers import WorkoutSerializer


# Create your views here.
class Workouts(generics.ListCreateAPIView):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer