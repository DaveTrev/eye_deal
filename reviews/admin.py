from django.contrib import admin
from .models import Review


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'created_on',
        'product_type',
        'rating',
        'body_text',
    )

    ordering = ('created_on',)


admin.site.register(Review, ReviewsAdmin)