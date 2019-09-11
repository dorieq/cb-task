from django.contrib import admin
from api.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'title', 'created_by')


admin.site.unregister(Review)
admin.site.register(Review)
