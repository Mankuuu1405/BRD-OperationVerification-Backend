from django.db import models

class Rejected(models.Model):

    action = models.OneToOneField(
        'dashboard.PendingTask',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        limit_choices_to={'action': 'REJECTED'}
    )
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title