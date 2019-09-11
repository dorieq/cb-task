from django.db import models
from django.contrib.auth.models import User


class ReviewManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Review(models.Model):
    rating: models.IntegerField(default=1)
    title: models.CharField(max_length=64)
    summary: models.CharField(max_length=10000)
    ip: models.CharField()
    date: models.DateField()
    created_by: models.ForeignKey(User, on_delete=models.CASCADE)
    objects = ReviewManager
