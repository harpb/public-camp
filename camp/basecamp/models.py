
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


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

    def __str__(self):
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

    camp = models.ForeignKey('basecamp.Camp', on_delete=models.CASCADE, related_name='attendees')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    role = models.CharField(max_length=32, choices=ROLE_TYPES)

    class Meta:
        db_table = 'attendee'
        unique_together = (('camp', 'user'),)

    def __str__(self):
        return u'{}: {}'.format(self.camp.name, self.user.get_full_name() or self.user.username)


class Activity(models.Model):
    '''
    An activity should have a name, start datetime, end datetime, counselor that's leading it
    '''
    counselor = models.ForeignKey(
        Attendee,
        limit_choices_to={'role': Attendee.ROLE_COUNSELOR},
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    class Meta:
        db_table = 'activity'

    def __str__(self):
        return u'{0.name}: {0.start_at} - {0.end_at}'.format(self)


class ActivityAttendee(models.Model):
    '''
    List of attendees (registrants)
    '''
    activity = models.ForeignKey(
        Activity,
        related_name='attendees',
        on_delete=models.CASCADE
    )
    attendee = models.ForeignKey(
        Attendee,
        limit_choices_to={'role': Attendee.ROLE_CAMPER},
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'activity_attendee'
        unique_together = (('activity', 'attendee'),)
