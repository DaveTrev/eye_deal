from django.db import models


class Review(models.Model):
    customer_name = models.Charfield(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    product_type = models.CharField(max_length=50, choices=[('Glasses', 'Glasses'),
                                                    ('Sunglasses',
                                                    'Sunglasses')])
    body_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.full_name}"