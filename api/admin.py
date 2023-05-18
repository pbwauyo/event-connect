from django.contrib import admin
from .models import Event, Attendee
from django.core.paginator import Paginator
from django.core.cache import cache
from django.contrib.auth.models import Group, User

# for performance improvement when loading many fields
class CachingPaginator(Paginator):
    def _get_count(self):

        if not hasattr(self, "_count"):
            self._count = None

        if self._count is None:
            try:
                key = "adm:{0}:count".format(hash(self.object_list.query.__str__()))
                self._count = cache.get(key, -1)
                if self._count == -1:
                    self._count = super().count
                    cache.set(key, self._count, 3600)

            except:
                self._count = len(self.object_list)
        return self._count

    count = property(_get_count)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'time', 'location', 'description')
    search_fields = ('name',)

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'title', 'organisation', 'nin', 'phone', 'receivedTransport', 'receivedLunch')
    search_fields = ('firstName', 'lastName')

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)

