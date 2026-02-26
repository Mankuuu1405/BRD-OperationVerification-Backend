from django.db import models
from django.utils import timezone


class OperationsDashboard(models.Model):
    pending_tasks = models.IntegerField(default=0)
    completed_today = models.IntegerField(default=0)
    sla_breaches = models.IntegerField(default=0)
    ocr_failures = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dashboard Summary - {self.created_at.date()}"


class PendingTask(models.Model):

    TYPE_CHOICES = [
        ("KYC", "KYC"),
        ("OCR", "OCR"),
        ("SITE_VISIT", "Site Visit"),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    STATUS_CHOICES = [
        ("COMPLETE", "COMPLETE"),
        ("INPROGRESS", "inprogress"),
        ("REJECTED", "REJECTED"),
     
    ]

    task_id = models.CharField(max_length=20, unique=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    customer = models.CharField(max_length=200)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='low'
    )
    due_date = models.DateTimeField()
    action = models.CharField(max_length=20, choices=STATUS_CHOICES)



    # ✅ Auto Generate TASK-1001
    def save(self, *args, **kwargs):
        if not self.task_id:
            last_task = PendingTask.objects.order_by('-id').first()
            if last_task:
                last_id = int(last_task.task_id.split('-')[1])
                new_id = last_id + 1
            else:
                new_id = 1001

            self.task_id = f"TASK-{new_id}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.task_id

    @property
    def tat_remaining(self):
        remaining = self.due_date - timezone.now()
        total_seconds = int(remaining.total_seconds())
        hours = abs(total_seconds) // 3600
        minutes = (abs(total_seconds) % 3600) // 60
        if total_seconds > 0:
          return f"{hours}h {minutes}m remaining"
        else:
           return f"{hours}h {minutes}m overdue"