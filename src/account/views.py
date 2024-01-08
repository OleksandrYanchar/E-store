from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from payment.forms import ShippingForm
from payment.models import ShippingAddress, OrderItem

from .forms import CreateUserForm, LoginForm, UpdateUserForm
from .token import user_tokenizer_generate
from django.contrib import messages


def register(request):
    form = CreateUserForm

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = False

            user.save()

            current_site = get_current_site(request)

            subject = "Account verification"

            message = render_to_string(
                "account/registartion/email-varification.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": user_tokenizer_generate.make_token(user),
                },
            )

            user.email_user(subject=subject, message=message)

            return redirect("email-verification-sent")

    context = {"form": form}

    return render(request, "account/registartion/register.html", context=context)


def email_varification(request, uidb64, token):
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)

    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active = True

        user.save()

        return redirect("email-verification-success")
    else:
        return redirect("email-verification-failed")


def email_varification_sent(request):
    return render(request, "account/registartion/email-verification-sent.html")


def email_varification_success(request):
    return render(request, "account/registartion/email-verification-success.html")


def email_varification_failed(request):
    return render(request, "account/registartion/email-verification-fail.html")


def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {"form": form}

    return render(request, "account/my-login.html", context=context)


def user_logout(request):
    try:
        for key in list(request.session.keys()):
            if key == "session_key":
                continue
            else:
                del request.session[key]

    except KeyError:
        pass

    messages.success(request, "Logout success")

    return redirect("store")


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, "account/dashboard.html")


@login_required(login_url="my-login")
def delete_account(request):
    user = User.objects.get(id=request.user.id)

    if request.method == "POST":
        user.delete()

        messages.error(request, "Account deleted")

        return redirect("delete-success")

    return render(request, "account/delete-account.html")


@login_required(login_url="my-login")
def profile_managment(request):
    user_form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.info(request, "Information changed")

            return redirect("dashboard")

    context = {"user_form": user_form}

    return render(request, "account/profile-managment.html", context=context)


def delete_success(request):
    return render(request, "account/delete-success.html")


@login_required(login_url="my-login")
def manage_shipping(request):
    try:
        shipping = ShippingAddress.objects.get(user=request.user.id)

    except ShippingAddress.DoesNotExist:
        shipping = None

    form = ShippingForm(instance=shipping)

    if request.method == "POST":
        form = ShippingForm(request.POST, instance=shipping)

        if form.is_valid():
            shipping_user = form.save(commit=False)

            shipping_user.user = request.user

            shipping_user.save()

            return redirect("dashboard")

    context = {"form": form}

    return render(request, "account/manage-shipping.html", context=context)


@login_required(login_url="my-login")
def track_orders(request):
    try:
        orders = OrderItem.objects.filter(user=request.user)

        context = {"orders": orders}

        return render(request, "account/track-orders.html", context=context)

    except:
        return render(request, "account/track-orders.html")
