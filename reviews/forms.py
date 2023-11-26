from django import forms
from .models import Review


class PostReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('customer_name', 'email', 'product_type', 'rating', 'body_text',)