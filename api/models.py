from django.db import models

class Attendee(models.Model):
    firstName = models.CharField(verbose_name="Given Name", max_length=100)
    lastName = models.CharField(verbose_name="Surname", max_length=100)
    title = models.CharField(verbose_name="Title", max_length=100)
    gender = models.CharField(verbose_name='Gender', max_length=10, null=True)
    organisation = models.CharField(verbose_name="Organisation", max_length=100)
    nin = models.CharField(verbose_name="NIN", max_length=100)
    phone = models.CharField(verbose_name="Phone", max_length=100)
    arrivalTime = models.TimeField(verbose_name='Arrival Time', auto_now_add=True, null=True, blank=True)
    receivedTransport = models.BooleanField(verbose_name="Received Transport",default=False)
    receivedLunch = models.BooleanField(verbose_name="Receieved Lunch", default=False)
    eventId = models.ForeignKey('Event', blank=True, on_delete=models.CASCADE, null=True, verbose_name="Event")

    def __str__(self) -> str:
        return self.firstName + ' ' + self.lastName
    
class Event(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    date = models.DateField(verbose_name="Date")
    time  = models.TimeField(verbose_name="Time")
    location = models.CharField(verbose_name="Location", max_length=100)
    description = models.TextField(verbose_name="Description")
    attendees = models.ManyToManyField('Attendee', blank=True)

    def __str__(self) -> str:
        return self.name
    
class Facilities(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)

    def __str__(self) -> str:
        return self.name

class Reports(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Dashboard(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)

    def __str__(self) -> str:
        return self.name

class Client(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name  
