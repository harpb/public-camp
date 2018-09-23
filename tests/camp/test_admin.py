from django.urls import reverse
from django.utils.functional import cached_property

from camp.basecamp.models import Attendee, Camp
from tests.test_cases import ViewTestCase


class CampAdminTests(ViewTestCase):

    def test_success__create(self):
        payload = dict(
            name='HarpLyfe',
            start_at_0='2018-06-01',
            start_at_1='00:00:00',
            end_at_0='2018-08-01',
            end_at_1='00:00:00',
        )
        # CALL
        response = self.client.post(
            path=reverse('admin:basecamp_camp_add'),
            data=payload
        )
        # ASSERT
        self.assertEqual(302, response.status_code)
        self.assertEqual(
            reverse('admin:basecamp_camp_changelist'),
            response.url
        )

    def test_fail__end_at_before_start_at(self):
        payload = dict(
            name='HarpLyfe',
            start_at_0='2018-06-01',
            start_at_1='00:00:00',
            end_at_0='2018-05-01',
            end_at_1='00:00:00',
        )
        # CALL
        response = self.client.post(
            path=reverse('admin:basecamp_camp_add'),
            data=payload
        )
        # ASSERT
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            'Camp must end after it starts.',
            response.context_data['errors'][0][0]
        )


class ActivityAdminTests(ViewTestCase):
    fixtures = ['users.yaml', 'camps.yaml']

    @cached_property
    def counselor_harp(self):
        return Attendee.objects.get(user__username='harp')

    def test_success__get(self):
        # CALL
        response = self.client.get(path=reverse('admin:basecamp_activity_changelist'))
        # ASSERT
        self.assertEqual(200, response.status_code)

    def test_success__create(self):
        payload = dict(
            name='Lunch',
            counselor=self.counselor_harp.id,
            start_at_0='2018-06-01',
            start_at_1='12:00:00',
            end_at_0='2018-06-01',
            end_at_1='13:00:00',
        )
        # CALL
        response = self.client.post(
            path=reverse('admin:basecamp_activity_add'),
            data=payload
        )
        # ASSERT
        self.assertEqual(302, response.status_code)
        self.assertEqual(
            reverse('admin:basecamp_activity_changelist'),
            response.url
        )

    def test_success__create_all_hands_meetings(self):
        payload = dict(
            name='All-hands Meeting',
            counselor=self.counselor_harp.id,
            start_at_0='2018-06-01',
            start_at_1='12:00:00',
            end_at_0='2018-06-01',
            end_at_1='13:00:00',
        )
        # CALL
        response = self.client.post(
            path=reverse('admin:basecamp_activity_add'),
            data=payload
        )
        # ASSERT
        self.assertEqual(302, response.status_code)
        self.assertEqual(
            reverse('admin:basecamp_activity_changelist'),
            response.url
        )

    def test_fail__end_at_before_start_at(self):
        payload = dict(
            name='Lunch',
            counselor=self.counselor_harp.id,
            start_at_0='2018-06-01',
            start_at_1='12:00:00',
            end_at_0='2018-06-01',
            end_at_1='12:00:00',
        )
        # CALL
        response = self.client.post(
            path=reverse('admin:basecamp_activity_add'),
            data=payload
        )
        # ASSERT
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            'Activity must end after it starts.',
            response.context_data['errors'][0][0]
        )

    def test_fail__start_before_camp(self):
        payload = dict(
            name='Lunch',
            counselor=self.counselor_harp.id,
            start_at_0='2018-05-01',
            start_at_1='12:00:00',
            end_at_0='2018-06-01',
            end_at_1='12:00:00',
        )
        # CALL
        response = self.client.post(
            path=reverse('admin:basecamp_activity_add'),
            data=payload
        )
        # ASSERT
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            'Activity must start after camp starts.',
            response.context_data['errors'][0][0]
        )

    def test_fail__ends_after_camp(self):
        payload = dict(
            name='Lunch',
            counselor=self.counselor_harp.id,
            start_at_0='2018-08-01',
            start_at_1='12:00:00',
            end_at_0='2019-08-01',
            end_at_1='12:00:00',
        )
        # CALL
        response = self.client.post(
            path=reverse('admin:basecamp_activity_add'),
            data=payload
        )
        # ASSERT
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            'Activity must end before camp ends.',
            response.context_data['errors'][0][0]
        )