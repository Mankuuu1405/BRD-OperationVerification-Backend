from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Count, Q

from .models import OperationsDashboard, PendingTask
from .serializers import (
    OperationsDashboardSerializer,
    PendingTaskSerializer
)

from rest_framework import viewsets

class PendingTaskViewSet(viewsets.ModelViewSet):
    queryset = PendingTask.objects.all()
    serializer_class = PendingTaskSerializer

    # ✅ For SiteVisit Page
    @action(detail=False, methods=["get"])
    def sitevisit(self, request):
        tasks = PendingTask.objects.filter(
            type="SITE_VISIT",
            action__in=["COMPLETE", "INPROGRESS"]
        )
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    # ✅ For Rejected Page
    @action(detail=False, methods=["get"])
    def rejected(self, request):
        tasks = PendingTask.objects.filter(
            type="rejected",
            action="REJECTED"
        )
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
class OperationsDashboardViewSet(viewsets.ViewSet):

    def list(self, request):

        total_tasks = PendingTask.objects.count()

        ocr_tasks = PendingTask.objects.filter(
            task_type="OCR"
        ).count()

        data = {
            "total_tasks": total_tasks,
            "ocr_tasks": ocr_tasks,
        }

        return Response(data)