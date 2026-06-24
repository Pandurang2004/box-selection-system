from django.urls import path
from .views import RecommendBoxAPIView

urlpatterns = [
    path(
        "recommend/",
        RecommendBoxAPIView.as_view(),
        name="recommend-box"
    ),
]
