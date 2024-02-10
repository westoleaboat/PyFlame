from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


class TestAuthentication(TestCase):
    def test_authenticated_workflow(self):
        # Creates a test user account for Bob
        passphrase = 'wool reselect resurface annuity'
        get_user_model().objects.create_user('bob', password=passphrase)
        # Bob logs in.
        self.client.login(username='bob', password=passphrase)
        self.assertIn('sessionid', self.client.cookies)
        # Accesses Bob’s profile page
        response = self.client.get(
            '/accounts/profile/',
            secure=True)  # Simulates HTTPS
        # Verifies the response
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'bob')
        self.client.logout()
        # Verifies Bob is logged out
        self.assertNotIn('sessionid', self.client.cookies)

    def test_prohibit_anonymous_access(self):
        # Attempts anonymous access
        response = self.client.get('/accounts/profile/', secure=True)
        # Verifies the response
        self.assertEqual(302, response.status_code)
        self.assertIn('/accounts/login/', response['Location'])
