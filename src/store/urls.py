from django.urls import path

from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("product/<slug:slug>", views.poduct_info, name="poduct-info"),
    path("search/<slug:category_slug>", views.list_category, name="list-category"),
]
