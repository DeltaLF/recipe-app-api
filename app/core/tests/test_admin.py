"""
Tests for the Django admin modifications
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin"""

    def setUp(self):
        """Create user and clients"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="password"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="password",
            name="Test User"
        )

    def test_users_list(self):
        """Tests that users are listed on page"""
        # reverse method is used to get the actual url
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
