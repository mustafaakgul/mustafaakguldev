from django.contrib import admin
from .models import Contact, Newsletter, Project


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]
    list_display_links = ["subject"]
    search_fields = ["subject"]
    list_filter = ["created_date"]

    class Meta:
        model = Contact


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Newsletter._meta.fields]
    list_display_links = ["email"]
    search_fields = ["email"]
    list_filter = ["created_date"]

    class Meta:
        model = Newsletter


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]
    list_display_links = ["title"]
    search_fields = ["title", "description"]
    list_filter = ["created_date"]

    class Meta:
        model = Project