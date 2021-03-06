from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Review


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    created_by = UserSerializer(read_only=True)
    date = serializers.DateField()
    
    class Meta:
        model = Review
        fields = ('id', 'rating', 'title', 'date',)
