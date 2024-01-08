from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    # Register and login urls
    path("register", views.register, name="register"),
    path("my-login", views.my_login, name="my-login"),
    path("user-logout", views.user_logout, name="user-logout"),
    # Email verivication views urls
    path(
        "email-verification/<str:uidb64>/<str:token>",
        views.email_varification,
        name="email-verification",
    ),
    path(
        "email-verification-sent",
        views.email_varification_sent,
        name="email-verification-sent",
    ),
    path(
        "email-verification-success",
        views.email_varification_success,
        name="email-verification-success",
    ),
    path(
        "email-verification-failed",
        views.email_varification_failed,
        name="email-verification-failed",
    ),
    # Profile managment urls
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile-managment", views.profile_managment, name="profile-managment"),
    path("delete-account", views.delete_account, name="delete-account"),
    path("delete-success", views.delete_success, name="delete-success"),
    # Password management urls/views
    path(
        "reset_password",
        auth_views.PasswordResetView.as_view(
            template_name="account/password/password-reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password/password-reset-sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password/password-reset-form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password/password-reset-complete.html"
        ),
        name="password_reset_complete",
    ),
    # Manage shipping urls
    path("manage-shipping", views.manage_shipping, name="manage-shipping"),
    path("track-orders", views.track_orders, name="track-orders"),
]
