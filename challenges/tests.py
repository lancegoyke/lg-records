from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Challenge, Record

# Create your tests here.
class ChallengeTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='recorduser',
            email='recorduser@email.com',
            password='testpass123'
        )

        self.adminuser = get_user_model().objects.create_superuser(
            username='adminuser',
            email='adminuser@email.com',
            password='testpass123'
        )

        self.challenge = Challenge.objects.create(
            name='Test challenge',
            description='This is a hard workout',
            tags=[],
        )

        self.record = Record.objects.create(
            challenge = self.challenge,
            user = self.user,
            time_score = '4:26:44',
        )
    
    
    def test_challenge_listing(self):
        self.assertEqual(f'{self.challenge.name}', 'Test challenge')
        self.assertEqual(f'{self.challenge.description}', 'This is a hard workout')


    def test_challenge_list_view_for_logged_in_user(self):
        self.client.login(email='recorduser@email.com', password='testpass123')
        response = self.client.get(reverse('challenge_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test challenge'.title())
        self.assertNotContains(response, 'Test challenge'.lower())
        self.assertTemplateUsed(response, 'challenges/challenge_list.html')
        self.assertContains(response, 'Search')


    def test_challenge_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('challenge_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '%s?next=/challenges/' % (reverse('account_login'))
        )
        response = self.client.get(
            '%s?next=/challenges/' % (reverse('account_login'))
        )
        self.assertContains(response, 'Log In')

    
    def test_challenge_detail_view_for_logged_in_user(self):
        self.client.login(email='recorduser@email.com', password='testpass123')
        response = self.client.get(self.challenge.get_absolute_url())
        no_response = self.client.get('/challenges/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test challenge'.title())
        self.assertNotContains(response, 'Test challenge'.lower())
        self.assertContains(response, 'This is a hard workout')
        self.assertContains(response, 'recorduser')
        self.assertContains(response, '4:26:44')
        self.assertTemplateUsed(response, 'challenges/challenge_detail.html')
        
        
    def test_challenge_detail_view_for_logged_in_superuser(self):
        self.client.logout()
        self.client.login(email='adminuser@email.com', password='testpass123')
        response = self.client.get(self.challenge.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test challenge'.title())
        self.assertNotContains(response, 'Test challenge'.lower())
        self.assertContains(response, 'This is a hard workout')
        self.assertContains(response, 'Update')


    def test_challenge_detail_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(self.challenge.get_absolute_url())
        self.assertEqual(response.status_code, 302)


    def test_challenge_update_view_for_logged_in_adminuser(self):
        self.client.login(email='adminuser@email.com', password='testpass123')
        response = self.client.get(reverse('challenge_update', kwargs={"slug":self.challenge.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test challenge'.title())
        self.assertContains(response, 'This is a hard workout')
        self.assertNotContains(response, 'Test challenge'.lower())
        self.assertTemplateUsed(response, 'challenges/challenge_update.html')
        self.assertContains(response, 'Update')


    def test_challenge_update_view_for_logged_in_user(self):
        self.client.login(email='recorduser@email.com', password='testpass123')
        response = self.client.get(reverse('challenge_update', kwargs={"slug":self.challenge.slug}))
        self.assertEqual(response.status_code, 403)


    def test_challenge_create_view_for_logged_in_adminuser(self):
        self.client.login(email='adminuser@email.com', password='testpass123')
        response = self.client.get(reverse('challenge_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'challenges/challenge_create.html')
        self.assertContains(response, 'Create')


    def test_challenge_create_view_for_logged_in_user(self):
        self.client.login(email='recorduser@email.com', password='testpass123')
        response = self.client.get(reverse('challenge_create'))
        self.assertEqual(response.status_code, 403)