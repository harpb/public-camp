
from django.contrib import admin

from camp.basecamp.forms import CampAdminForm
from camp.basecamp.models import Attendee
from camp.basecamp.models import Camp


class CampAdmin(admin.ModelAdmin):
    '''
    Admin for camp details
    '''
    form = CampAdminForm

    list_display = ['name', 'start_at', 'end_at']

    search_fields = ['name']


class AttendeeAdmin(admin.ModelAdmin):
    '''
    Admin for camp attendees
    '''
    list_display = ['camp', 'user', 'role']

    search_fields = [
        'camp__name',
        'role',
        'user__email',
        'user__first_name',
        'user__last_name',
        'user__username'
    ]


# Register admin views here
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Camp, CampAdmin)
