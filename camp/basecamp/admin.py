
from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from camp.basecamp.forms import CampAdminForm, ActivityAdminForm
from camp.basecamp.models import Attendee, Activity, ActivityAttendee
from camp.basecamp.models import Camp


@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    '''
    Admin for camp details
    '''
    form = CampAdminForm

    list_display = ['name', 'start_at', 'end_at']

    search_fields = ['name']


@admin.register(Attendee)
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


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    '''
    Admin panel for activities that allows you to create/edit/update/delete an activity, as well as see all the people attending.
    '''
    form = ActivityAdminForm
    list_display = ['id', 'name', 'counselor', 'start_at', 'end_at', 'get_registrants']

    def get_registrants(self, obj):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            [(activity_attendee.attendee,) for activity_attendee in obj.attendees.all()]
        )
    get_registrants.short_description = "Registrants"
    get_registrants.allow_tags = True

    search_fields = [
        'counselor__user__username',
        'name'
    ]


@admin.register(ActivityAttendee)
class ActivityAttendeeAdmin(admin.ModelAdmin):
    '''
    Admin panel for activity registrations that allows you to create/edit/update/delete an activity registration.
    '''
    list_display = ['id', 'activity', 'attendee']

    search_fields = [
        'activity__name',
        'attendee__camp__name',
        'attendee__user__username',
    ]
