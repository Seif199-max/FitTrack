from django.urls import path
from .views import Workouts
urlpatterns = [


    path('workouts',Workouts.as_view()),

]