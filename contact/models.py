from django.db import models

CONTACT_REASONS = (
    ("general_query", "General Query"),
    ("glasses", "Glasses"),
    ("sunglasses", "Sunglasses"),
    ("technical_issue", "Technical Issue"),
    ("other", "Other"),
)


class Contact(models.Model):

    contact_reason = models.CharField(
        max_length=100,
        choices=CONTACT_REASONS,
        default="general_query",
        null=False,
        blank=False,
    )
    name = models.CharField(null=False, blank=False, max_length=50,)
    email = models.EmailField(null=False, blank=False, max_length=250,)
    message = models.TextField(max_length=400, null=False, blank=False,)

    def __str__(self):
        return f"{self.name} - {self.email}"
