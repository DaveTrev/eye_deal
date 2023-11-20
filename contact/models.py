from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.name} - {self.email}"