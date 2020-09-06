from django.db import models

# Create your models here.


class Feedback(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    comment = models.TextField(max_length=3000, default="Enter your feedback")
