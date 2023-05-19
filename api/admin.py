from django.contrib import admin
from .models import *
from django.core.paginator import Paginator
from django.core.cache import cache
from django.contrib.auth.models import Group, User
from import_export.admin import ExportActionMixin

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

class EventAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'time', 'location', 'description')
    search_fields = ('name',)
    ordering = ('id',)

class AttendeeAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','firstName', 'lastName', 'title', 'organisation', 'nin', 'phone', 'arrivalTime', 'eventId', 'receivedTransport', 'receivedLunch')
    search_fields = ('firstName', 'lastName')
    ordering = ('id',)

class FacilitiesAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

class ReportsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('id',)

class DashboardAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('id',)

class ClientAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    search_fields = ('first_name', 'last_name')
    ordering = ('id',)


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Facilities, FacilitiesAdmin)
admin.site.register(Reports, ReportsAdmin)
admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(Client, ClientAdmin)

