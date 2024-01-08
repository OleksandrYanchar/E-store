from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Product

from .cart import Cart


def cart_summary(request):
    return render(request, "cart/cart-summary.html")


def cart_add(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, product_qty=product_quantity)

        cart_quantity = cart.__len__()

        response = JsonResponse({"qty": cart_quantity})

    return response


def cart_delete(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))

        cart.delete(product=product_id)

        cart_quantity = cart.__len__()

        cart_total = cart.get_total()

        response = JsonResponse({"qty": cart_quantity, "total": cart_total})

    return response


def cart_update(request):
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))

        cart.update(product=product_id, qty=product_quantity)

        cart_quantity = cart.__len__()
        cart_total = cart.get_total()

        response = JsonResponse({"qty": cart_quantity, "total": cart_total})

    return response
