from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from user.serializers import UserSerializer

class UserView(generics.ListCreateAPIView):
	def get_queryset(self):
		return User.objects.all()

	def get_serializer_class(self):
		return UserSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			if User.objects.filter(username=self.request.user.username, groups=(2, )):
				return IsAuthenticated()

			return IsAdminUser()

		elif self.request.method == 'POST':
			return AllowAny()