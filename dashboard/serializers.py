from rest_framework import serializers
from .models import OperationsDashboard, PendingTask

class OperationsDashboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperationsDashboard
        fields = [
            'pending_tasks',
            'completed_today',
            'sla_breaches',
            'ocr_failures',
            'created_at'
        ]
        read_only_fields = ['created_at']

class PendingTaskSerializer(serializers.ModelSerializer):

    tat_remaining = serializers.ReadOnlyField()

    class Meta:
        model = PendingTask
        fields = '__all__'

    