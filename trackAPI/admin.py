from django.contrib import admin

from .models import Workout,Meal,DailySummary

# Register your models here.
admin.site.register(Workout)
admin.site.register(Meal)
admin.site.register(DailySummary)
