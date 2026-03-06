from rest_framework import viewsets
from .models import OperationsDashboard, PendingTask
from .serializers import OperationsDashboardSerializer, PendingTaskSerializer


class OperationsDashboardViewSet(viewsets.ModelViewSet):
    queryset = OperationsDashboard.objects.all().order_by("-created_at")
    serializer_class = OperationsDashboardSerializer


class PendingTaskViewSet(viewsets.ModelViewSet):
    queryset = PendingTask.objects.all().order_by("due_date")
    serializer_class = PendingTaskSerializer
