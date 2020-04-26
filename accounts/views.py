from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm, CustomerForm
from .models import Customer


# Create your views here.
# def index(request):
#     """A view that displays the index page"""
#     return render(request, "index.html")


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


# @login_required
# def profile(request):
#     """
#     A view that displays the profile page of a logged in user
#     """
#     return render(request, 'profile.html')


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
    Shows the customer their current profile details.
    Allows the customer to update their profile details.
    Creates a new customer on completion.
    """

    customer = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        profile_form = CustomerForm(request.POST, instance=customer)
        if profile_form.is_valid():
            customer = profile_form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request,
                             "Your profile has been updated successfully")
    else:
        profile_form = CustomerForm(instance=customer)

    args = {"profile_form": profile_form}
    return render(request, "profile.html", args)
