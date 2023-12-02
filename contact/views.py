from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f'The Contact message was sent!')
            return render(request, 'contact/contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
