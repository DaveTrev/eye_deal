from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Review
from .forms import PostReviewForm


def reviews(request):
    """ A view to return the reviews page """

    reviews = Review.objects.all()

    if request.method == 'POST':
        form = PostReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for posting a review!')
            return redirect('reviews')
        else:
            messages.warning(request, 'Failed to post the review. Score is out of 5/5.')
    else:
        form = PostReviewForm()

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, template, context)

