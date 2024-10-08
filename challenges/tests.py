from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Challenge, Record


# Create your tests here.
class ChallengeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="recorduser", email="recorduser@email.com", password="testpass123"
        )

        self.adminuser = get_user_model().objects.create_superuser(
            username="adminuser", email="adminuser@email.com", password="testpass123"
        )

        self.challenge = Challenge.objects.create(
            name="Test challenge",
            description="This is a hard workout",
            tags=[],
        )

        self.record = Record.objects.create(
            challenge=self.challenge,
            user=self.user,
            time_score="4:26:44",
        )

    def test_challenge_listing(self):
        self.assertEqual(f"{self.challenge.name}", "Test challenge")
        self.assertEqual(f"{self.challenge.description}", "This is a hard workout")

    def test_challenge_list_view_for_logged_in_user(self):
        self.client.login(email="recorduser@email.com", password="testpass123")
        response = self.client.get(reverse("challenge_filtered_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test challenge")
        self.assertTemplateUsed(response, "challenges/challenge_filtered_list.html")
        self.assertContains(response, "Search")

    def test_challenge_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("challenge_filtered_list"))
        self.assertEqual(response.status_code, 302)

    def test_challenge_detail_view_for_logged_in_user(self):
        self.client.login(email="recorduser@email.com", password="testpass123")
        response = self.client.get(self.challenge.get_absolute_url())
        no_response = self.client.get("/challenges/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test challenge")
        self.assertContains(response, "This is a hard workout")
        self.assertContains(response, "recorduser")
        self.assertContains(response, "4:26:44")
        self.assertTemplateUsed(response, "challenges/challenge_detail.html")

    def test_challenge_detail_view_for_logged_in_superuser(self):
        self.client.logout()
        self.client.login(email="adminuser@email.com", password="testpass123")
        response = self.client.get(self.challenge.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test challenge")
        self.assertContains(response, "This is a hard workout")

    def test_challenge_detail_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(self.challenge.get_absolute_url())
        self.assertEqual(response.status_code, 302)

    def test_challenge_detail_view_record_create_form(self):
        # make sure logged in user can submit record
        self.client.login(email="recorduser@email.com", password="testpass123")
        response = self.client.post(
            self.challenge.get_absolute_url(),
            kwargs={
                "form": {
                    "time_score": "01",
                    "notes": "I did it at the speed of light",
                }
            },
        )
        response = self.client.get(self.challenge.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("challenges/challenge_detail.html")
        self.assertContains(response, "recorduser")

        # make sure submitted record shows up afterwards
        # TODO

    def test_challenge_create_view_for_logged_in_adminuser(self):
        self.client.login(email="adminuser@email.com", password="testpass123")
        response = self.client.get(reverse("challenge_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "challenges/challenge_create.html")
        self.assertContains(response, "Create")

    def test_challenge_create_view_for_logged_in_user(self):
        self.client.login(email="recorduser@email.com", password="testpass123")
        # with self.assertRaises(PermissionDenied):
        response = self.client.get(reverse("challenge_create"))
        self.assertEqual(response.status_code, 403)
