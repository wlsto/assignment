from django.contrib import admin
from .models import Tweet, Like


# Register your models here.
class TweetElonFilter(admin.SimpleListFilter):
    title = "Filter by Elon Musk!"
    parameter_name = "filterOn"

    def lookups(self, request, model_admin):
        return [
            ("A", "Elon Musk"),
            ("B", "Not Elon Musk"),
        ]

    def queryset(self, request, reviews):
        filterOn = self.value()

        if filterOn == "A":
            return reviews.filter(payload__icontains="elon musk")
        elif filterOn == "B":
            return reviews.exclude(payload__icontains="elon musk")
        else:
            reviews


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "total_likes",
    )

    list_filter = (
        TweetElonFilter,
        "created_at",
    )

    search_fields = (
        "payload",
        "=user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_at",
        "updated_at",
    )

    list_filter = ("created_at",)

    search_fields = ("=user__username",)
