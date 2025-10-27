from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="مدة التمرين بالدقائق")
    calories_burned = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    time = models.TimeField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class DailySummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    total_meal_calories = models.PositiveIntegerField(default=0)
    total_burned_calories = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

    class Meta:
        unique_together = ('user', 'date')
