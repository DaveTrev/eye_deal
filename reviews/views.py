from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import PostReviewForm


@login_required
def reviews(request):
    """ A view to return the reviews page """

    reviews = Review.objects.all()

    if request.method == 'POST':
        form = PostReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for posting a review!')
            return redirect(reverse('reviews'))
        else:
            form = PostReviewForm()

    form = PostReviewForm()
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'reviews/reviews.html', context)