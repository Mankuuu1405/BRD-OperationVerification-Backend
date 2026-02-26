from rest_framework.routers import DefaultRouter
from .views import PendingTaskViewSet, OperationsDashboardViewSet

router = DefaultRouter()
router.register(r"tasks", PendingTaskViewSet)
router.register(r'dashboard', OperationsDashboardViewSet, basename='dashboard')

urlpatterns = router.urls