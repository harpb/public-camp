
from django.contrib.auth.models import User
from django.db import models


class Camp(models.Model):
    '''
    Camp is the thing everyone goes to in the summer to have fun
    '''
    name = models.CharField(max_length=256)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'camp'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Attendee(models.Model):
    '''
    Attendee is a person who attends a Camp
    '''
    ROLE_COUNSELOR = 'counselor'
    ROLE_CAMPER = 'camper'

    ROLE_TYPES = (
        (ROLE_COUNSELOR, 'Counselor'),
        (ROLE_CAMPER, 'Camper')
    )

    camp = models.ForeignKey('basecamp.Camp')
    user = models.ForeignKey('auth.User')
    role = models.CharField(max_length=32, choices=ROLE_TYPES)

    class Meta:
        db_table = 'attendee'
        unique_together = (('camp', 'user'),)

    def __unicode__(self):
        return u'{}: {}'.format(self.camp.name, self.user.get_full_name())
