from django.contrib import admin
from .models import SiteVisitReport, SiteVisitPhoto, Recommendation, Rejected


# ✅ Inline Photos inside Report
class SiteVisitPhotoInline(admin.TabularInline):
    model = SiteVisitPhoto
    extra = 1


# ✅ Inline Recommendations inside Report
class RecommendationInline(admin.TabularInline):
    model = Recommendation
    extra = 1


@admin.register(SiteVisitReport)
class SiteVisitReportAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "location",
        "visit_date",
        "status",
        "created_at",
        "photos_count",
    )

    list_filter = ("status", "visit_date")
    search_fields = ("title", "location")
    readonly_fields = ("created_at",)

    inlines = [SiteVisitPhotoInline, RecommendationInline]
@admin.register(Rejected)
class RejectedAdmin(admin.ModelAdmin):

    list_display = (
       "action",
       "title",
    )

@admin.register(SiteVisitPhoto)
class SiteVisitPhotoAdmin(admin.ModelAdmin):
    list_display = ("report", "uploaded_at")
    list_filter = ("uploaded_at",)


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("report", "text")
    search_fields = ("text",)