from django.contrib import admin
from .models import OperationsDashboard, PendingTask


@admin.register(OperationsDashboard)
class OperationsDashboardAdmin(admin.ModelAdmin):
    list_display = (
        'pending_tasks',
        'completed_today',
        'sla_breaches',
        'ocr_failures',
        'created_at'
    )


@admin.register(PendingTask)
class PendingTaskAdmin(admin.ModelAdmin):
    list_display = (
        'task_id',
        'type',
        'customer',
        'priority',
        'tat_remaining',
        'action',
        
    )


 