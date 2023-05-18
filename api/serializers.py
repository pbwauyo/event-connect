from rest_framework import serializers
from .models import Attendee, Event

class AttendeeSerializer(serializers.ModelSerializer):
    attendee_events = serializers.SerializerMethodField()

    def get_attendee_events(self, attendee):
        return [
            {
                "name" : event.name,
                "id" : event.id
            } for event in attendee.events.all()
        ]

    class Meta:
        model = Attendee
        exclude = ['events']


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