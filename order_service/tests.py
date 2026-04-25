from django.test import TestCase

class OrderHealthTest(TestCase):
    def test_order_health(self):
        response = self.client.get("/order/health/")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {"status": "ok", "service": "order-service"}
        )

