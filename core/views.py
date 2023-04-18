from django.shortcuts import render, redirect, reverse
from .forms import ContactForm, NewsletterForm
from django.contrib import messages


def index(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "index.html", context)


def page_404(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "404-page.html", context)


def about(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "about.html", context)


def blog_details(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "blog-details.html", context)


def blog_list_sidebar_right(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "blog-list-sidebar-right.html", context)


def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        "contact_form": contact_form,
    }

    return render(request, "contact.html", context)


def faq(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "faq.html", context)


def project_details(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "project-details.html", context)


def project_list(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "project-list.html", context)


def service_details(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "service-details.html", context)


def service_list(request):

    context = {
        "hello": "hello world"
    }

    return render(request, "service-list.html", context)


def add_contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        "contact_form": contact_form
    }

    if contact_form.is_valid():
        contact = contact_form.save(commit=False)
        contact.save()
        messages.success(request, "Contact form created successfully.")
        return redirect("contact")

    return render(request, "contact.html", context)


def add_newsletter(request):
    newsletter_form = NewsletterForm(request.POST or None)

    context = {
        "newsletter_form": newsletter_form
    }

    if newsletter_form.is_valid():
        newsletter = newsletter_form.save(commit=False)
        newsletter.save()
        messages.success(request, "Newsletter form created successfully.")
        return redirect("index")

    return render(request, "index.html", context)