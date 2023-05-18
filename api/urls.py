from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='api-events')
router.register(r'attendees', AttendeeViewSet, basename='api-attendees')

urlpatterns = router.urls

urlpatterns += [
    path('sample/', sample, name="api-sample")
]