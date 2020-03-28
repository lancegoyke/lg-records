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

        self.challenge = Challenge.objects.create(
            name='Test challenge',
            description='This is a hard workout',
        )

        self.record = Record.objects.create(
            challenge = self.challenge,
            user = self.user,
            time_score = '4:26:44',
        )
    
    
    def test_challenge_listing(self):
        self.assertEqual(f'{self.challenge.name}', 'Test challenge')
        self.assertEqual(f'{self.challenge.description}', 'This is a hard workout')


    def test_challenge_list_view(self):
        response = self.client.get(reverse('challenge_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test challenge')
        self.assertTemplateUsed(response, 'challenges/challenge_list.html')

    
    def test_challenge_detail_view(self):
        response = self.client.get(self.challenge.get_absolute_url())
        no_response = self.client.get('/challenges/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test challenge')
        self.assertContains(response, 'recorduser')
        self.assertContains(response, '4:26:44')
        self.assertTemplateUsed(response, 'challenges/challenge_detail.html')