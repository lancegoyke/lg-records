from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='lancebasic',
            email='lancebasic@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'lancebasic')
        self.assertEqual(user.email, 'lancebasic@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='lanceadmin',
            email='lanceadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'lanceadmin')
        self.assertEqual(user.email, 'lanceadmin@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)