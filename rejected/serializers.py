from rest_framework import serializers
from .models import Rejected
from dashboard.models import PendingTask


class RejectedSerializer(serializers.ModelSerializer):

    action = serializers.PrimaryKeyRelatedField(
        queryset=PendingTask.objects.filter(action="REJECTED")
    )

    class Meta:
        model = Rejected
        fields = "__all__"