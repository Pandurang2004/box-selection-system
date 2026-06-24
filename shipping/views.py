from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RecommendationSerializer
from .services import BoxRecommendationService


class RecommendBoxAPIView(APIView):

    def post(self, request):

        serializer = RecommendationSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data

        box = BoxRecommendationService.recommend(
            length=data["length"],
            width=data["width"],
            height=data["height"],
            weight=data["weight"]
        )

        if box is None:
            return Response(
                {
                    "message": "No suitable box found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {
                "recommended_box": box.name,
                "cost": str(box.cost),
                "box_dimensions": {
                    "length": box.length,
                    "width": box.width,
                    "height": box.height
                },
                "max_weight": box.max_weight
            }
        )