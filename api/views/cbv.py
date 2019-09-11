from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Review
from api.serializers import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Review.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        remote_address = self.request.META.get('REMOTE_ADDR')
        ip = remote_address
        serializer.save(created_by=self.request.user, ip=ip)
