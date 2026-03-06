from django.contrib import admin
from .models import SiteVisitReport, SiteVisitPhoto, Recommendation, Rejected


# -----------------------------
# Inline for Photos
# -----------------------------
class SiteVisitPhotoInline(admin.TabularInline):
    model = SiteVisitPhoto
    extra = 1
    fields = ("image", "uploaded_at")
    readonly_fields = ("uploaded_at",)


# -----------------------------
# Inline for Recommendations
# -----------------------------
class RecommendationInline(admin.TabularInline):
    model = Recommendation
    extra = 1
    fields = ("text",)


# -----------------------------
# Site Visit Report Admin
# -----------------------------
@admin.register(SiteVisitReport)
class SiteVisitReportAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "location",
        "visit_date",
        "status",
        "photos_count",
        "created_at",
    )

    list_filter = (
        "status",
        "visit_date",
        "created_at",
    )

    search_fields = (
        "title",
        "location",
        "observations",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("-created_at",)

    inlines = [
        SiteVisitPhotoInline,
        RecommendationInline,
    ]


# -----------------------------
# Site Visit Photo Admin
# -----------------------------
@admin.register(SiteVisitPhoto)
class SiteVisitPhotoAdmin(admin.ModelAdmin):
    list_display = ("report", "image", "uploaded_at")
    search_fields = ("report__title",)
    readonly_fields = ("uploaded_at",)


# -----------------------------
# Recommendation Admin
# -----------------------------
@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("text", "report")
    search_fields = ("text", "report__title")


# -----------------------------
# Rejected Documents Admin
# -----------------------------
@admin.register(Rejected)
class RejectedAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "reason",
        "doc_type",
        "frequency",
        "created_at",
    )

    list_filter = (
        "doc_type",
        "created_at",
    )

    search_fields = (
        "title",
        "reason",
        "description",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("-created_at",)