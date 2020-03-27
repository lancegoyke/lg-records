from django.test import Client, TestCase
from django.urls import reverse

from .models import Challenge

# Create your tests here.
class ChallengeTests(TestCase):

    def setUp(self):
        self.challenge = Challenge.objects.create(
            name='Test challenge',
            description='This is a hard workout',
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
        self.assertTemplateUsed(response, 'challenges/challenge_detail.html')