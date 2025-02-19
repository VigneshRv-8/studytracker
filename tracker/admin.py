from django.contrib import admin
from .models import Topic  # Import only the existing Topic model

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic_name', 'created_at')  # Display these fields in the admin panel
