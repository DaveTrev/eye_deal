from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NwrZLI9dxh4u5jGSTVc8ScFox9i1hqN37op53kJ2N8ubHUjNlZRAY5x2JudFLSWBaoFRY18Rblv8c82hMqmJcnE00eUQ7jdOY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)