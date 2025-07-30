from django.contrib import admin
from .models import Component, IssueRecord

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'status', 'date_of_purchase')
    list_filter = ('category',)
    search_fields = ('name',)

    def status(self, obj):
        return obj.status

admin.site.register(IssueRecord)
