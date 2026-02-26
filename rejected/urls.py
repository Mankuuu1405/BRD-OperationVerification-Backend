from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RejectedViewSet

router = DefaultRouter()
router.register(r'rejected', RejectedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]