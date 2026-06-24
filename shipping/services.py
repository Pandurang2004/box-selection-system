from .models import Box


class BoxRecommendationService:

    @staticmethod
    def recommend(length, width, height, weight):

        valid_boxes = []

        for box in Box.objects.all():

            fits_dimensions = (
                length <= box.length and
                width <= box.width and
                height <= box.height
            )

            fits_weight = weight <= box.max_weight

            if fits_dimensions and fits_weight:
                valid_boxes.append(box)

        if not valid_boxes:
            return None

        # Cheapest first, then smallest volume
        valid_boxes.sort(
            key=lambda box: (
                float(box.cost),
                box.volume
            )
        )

        return valid_boxes[0]