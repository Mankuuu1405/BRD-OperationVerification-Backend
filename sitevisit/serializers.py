from rest_framework import serializers
from .models import SiteVisitReport, SiteVisitPhoto, Recommendation, Rejected


class SiteVisitPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteVisitPhoto
        fields = ["id", "image", "uploaded_at"]


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ["id", "text"]

class RejectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rejected
        fields = ["action", "title"]



class SiteVisitReportSerializer(serializers.ModelSerializer):

    photos = SiteVisitPhotoSerializer(many=True, read_only=True)
    recommendations = RecommendationSerializer(many=True)
    photos_taken = serializers.SerializerMethodField()

    class Meta:
        model = SiteVisitReport
        fields = [
            "id",
            "title",
            "location",
            "visit_date",
            "status",
            "latitude",
            "longitude",
            "observations",
            "created_at",
            "photos",
            "photos_taken",
            "recommendations",
        ]

    def get_photos_taken(self, obj):
        return obj.photos.count()

    def create(self, validated_data):
        recommendations_data = validated_data.pop("recommendations", [])
        report = SiteVisitReport.objects.create(**validated_data)

        for rec in recommendations_data:
            Recommendation.objects.create(report=report, **rec)

        return report