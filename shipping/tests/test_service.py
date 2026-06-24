from django.test import TestCase

from shipping.models import Box
from shipping.services import BoxRecommendationService


class BoxRecommendationServiceTest(TestCase):

    def setUp(self):
        Box.objects.create(
            name="Small Box",
            length=10,
            width=10,
            height=10,
            max_weight=5,
            cost=50
        )

        Box.objects.create(
            name="Medium Box",
            length=20,
            width=20,
            height=20,
            max_weight=10,
            cost=80
        )

        Box.objects.create(
            name="Large Box",
            length=30,
            width=30,
            height=30,
            max_weight=20,
            cost=120
        )

    def test_small_box_selected(self):
        box = BoxRecommendationService.recommend(
            5, 5, 5, 2
        )

        self.assertEqual(box.name, "Small Box")

    def test_medium_box_selected(self):
        box = BoxRecommendationService.recommend(
            15, 15, 15, 5
        )

        self.assertEqual(box.name, "Medium Box")

    def test_large_box_selected(self):
        box = BoxRecommendationService.recommend(
            25, 25, 25, 10
        )

        self.assertEqual(box.name, "Large Box")

    def test_no_box_available(self):
        box = BoxRecommendationService.recommend(
            100, 100, 100, 100
        )

        self.assertIsNone(box)

    def test_weight_exceeds_capacity(self):
        box = BoxRecommendationService.recommend(
            5, 5, 5, 50
        )

        self.assertIsNone(box)