from django.contrib import admin
from .models import Rejected


@admin.register(Rejected)
class RejectedAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'action')
    search_fields = ('title',)