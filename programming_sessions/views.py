from .models import Meeting
from rest_framework import viewsets, permissions
from .serializers import MeetingSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset=Meeting.objects.all().order_by('id')
    serializer_class=MeetingSerializer
    permission_classes=[permissions.AllowAny]