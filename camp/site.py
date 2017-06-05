
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from camp.basecamp.admin import AttendeeAdmin
from camp.basecamp.admin import CampAdmin
from camp.basecamp.models import Attendee
from camp.basecamp.models import Camp


class CampAdminSite(AdminSite):
    '''
    This class handles registration for Django admin views
    '''

    # Django-defined constants
    site_header = 'Camp Admin'
    index_title = 'Home'
    site_title = 'Camp Admin'

    def __init__(self, *args, **kwargs):
        super(CampAdminSite, self).__init__(*args, **kwargs)

        # Register all the relevant sites
        self.register_sites()

    def register_sites(self):
        '''
        Register all the admin sites here
        '''
        # Django admin sites
        self.register(User, UserAdmin)

        # Pre-fab admin views
        self.register(Attendee, AttendeeAdmin)
        self.register(Camp, CampAdmin)

        # TIP: ADD NEW ADMIN SITES HERE!

admin_site = CampAdminSite()
