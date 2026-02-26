from rest_framework import viewsets
from .models import SiteVisitReport, SiteVisitPhoto, Recommendation
from .serializers import (
    SiteVisitReportSerializer,
    SiteVisitPhotoSerializer,
    RecommendationSerializer
)


class SiteVisitReportViewSet(viewsets.ModelViewSet):
    queryset = SiteVisitReport.objects.all().order_by("-created_at")
    serializer_class = SiteVisitReportSerializer


class SiteVisitPhotoViewSet(viewsets.ModelViewSet):
    queryset = SiteVisitPhoto.objects.all().order_by("-uploaded_at")
    serializer_class = SiteVisitPhotoSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer