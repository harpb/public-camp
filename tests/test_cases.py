from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.functional import cached_property


class ViewTestCase(TestCase):
    fixtures = ['users.yaml']
    default_password = 'Pa$$w0rd'
    # Subclass should set endpoint_name, which is used to auto-determine the url for the endpoint.
    endpoint_name = None

    def setUp(self):
        super(ViewTestCase, self).setUp()

        # Views Client
        self.client = self.client_class()
        self.login_admin()

    @cached_property
    def admin(self):
        return get_user_model().objects.get(username='harp')

    def login_admin(self):
        self.logout()
        response = self.client.login(
            username=self.admin.username,
            password=self.default_password)
        self.assertTrue(response)

    def logout(self):
        self.client.logout()