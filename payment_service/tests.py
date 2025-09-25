from django.test import TestCase
from django.urls import reverse

class AuthHealthTest(TestCase):
    def test_auth_health(self):
        response = self.client.get("/auth/health/")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {"status": "ok", "service": "auth-service"}
        )
