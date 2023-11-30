from django.shortcuts import render


def index(request):
    """ A view to return the index page"""
    return render(request, 'home/index.html')


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')


def returns(request):
    """ A view to return the returns policy page """

    return render(request, 'home/returns.html')