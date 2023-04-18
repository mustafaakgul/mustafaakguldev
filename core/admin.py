from django.contrib import admin
from .models import Contact, Newsletter


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