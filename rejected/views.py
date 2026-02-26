from rest_framework.viewsets import ModelViewSet
from .models import Rejected
from .serializers import RejectedSerializer


class RejectedViewSet(ModelViewSet):
    queryset = Rejected.objects.all()
    serializer_class = RejectedSerializer