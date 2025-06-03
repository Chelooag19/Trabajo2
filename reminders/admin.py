from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('content', 'important', 'createdAt')
    list_filter = ('important',)
    search_fields = ('content',)
    ordering = ('-important', 'createdAt')
