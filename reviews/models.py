from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


def validate_rating(value):
    if value < 0 or value > 5:
        raise ValidationError("Please rate from 1 to 5 stars.")


class Review(models.Model):
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), validate_rating]
    )
    product_type = models.CharField(max_length=50, choices=[('Glasses',
                                                            'Glasses'),
                                                            ('Sunglasses',
                                                            'Sunglasses')])
    body_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body_text} by {self.customer_name}"
