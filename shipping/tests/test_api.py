from rest_framework.test import APITestCase

from shipping.models import Box


class RecommendBoxAPITest(APITestCase):

    def setUp(self):
        Box.objects.create(
            name="Small Box",
            length=10,
            width=10,
            height=10,
            max_weight=5,
            cost=50
        )

    def test_api_success(self):
        response = self.client.post(
            "/api/recommend/",
            {
                "length": 5,
                "width": 5,
                "height": 5,
                "weight": 2
            },
            format="json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["recommended_box"],
            "Small Box"
        )

    def test_api_no_box_found(self):
        response = self.client.post(
            "/api/recommend/",
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 100
            },
            format="json"
        )

        self.assertEqual(response.status_code, 404)

    def test_invalid_payload(self):
        response = self.client.post(
            "/api/recommend/",
            {
                "length": -1,
                "width": 5,
                "height": 5,
                "weight": 2
            },
            format="json"
        )

        self.assertEqual(response.status_code, 400)