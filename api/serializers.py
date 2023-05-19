from rest_framework import serializers
from .models import Attendee, Event

class AttendeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendee
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    attendees_details = serializers.SerializerMethodField()
    attendees_count = serializers.SerializerMethodField()

    def get_attendees_details(self, event):
        return [
            {"name" : attendee.firstName + ' ' + attendee.lastName} for attendee in event.attendees.all()
        ]
    
    def get_attendees_count(self, event):
        return event.attendees.all().count()

    class Meta:
        model = Event
        exclude = ['attendees']