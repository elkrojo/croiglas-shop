from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm, BillingAddressForm
from .models import BillingAddress


# Create your views here.


@login_required
def logout(request):
    """
    A view that logs the user out and redirects
    back to the index page
    """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """
    A view that manages the login form
    """
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None,
                                    "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def register(request):
    """
    A view that manages the registration form
    """
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        register_form = UserRegistrationForm()

    args = {'register_form': register_form}
    return render(request, 'register.html', args)


@login_required
def profile(request):
    """
    Shows the customer their current billing address details.
    Allows the customer to update their billing address details.
    Creates a new billing address on completion.
    """

    billing_address = BillingAddress.objects.filter(user=request.user).first()
    if request.method == "POST":
        billing_form = BillingForm(request.POST, instance=billing_address)
        if billing_form.is_valid():
            billing_address = billing_form.save(commit=False)
            billing_address.user = request.user
            billing_address.save()
            messages.success(request,
                             "Your billing address has been updated successfully")
    else:
        billing_form = BillingAddressForm(instance=billing_address)

    args = {"billing_form": billing_form}
    return render(request, "profile.html", args)
