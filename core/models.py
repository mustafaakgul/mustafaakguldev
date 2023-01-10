from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name