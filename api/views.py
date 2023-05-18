from django.shortcuts import render
from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

class EventViewSet(ModelViewSet):
    http_method_names = ['get', 'post']

    serializer_class = EventSerializer
    queryset = Event.objects.all()

class AttendeeViewSet(ModelViewSet):
    http_method_names = ['get', 'post']

    serializer_class = AttendeeSerializer
    queryset = Attendee.objects.all()

@api_view(['GET'])
@permission_classes([AllowAny])
def sample(request):
    return Response({'message' : 'working'})