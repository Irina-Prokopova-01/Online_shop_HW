from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Product


def home(request: HttpRequest):
    """функция обрабатывает запрос и возвращает html-страницу"""
    if request.method == "GET":
        products = Product.objects.all()
        context = {"products": products}

        return render(request, "home.html", context=context)


def contacts(request):
    """Обрабатываем форму и возвращаем ответ"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"Спасибо, {name}, за Ваше сообщение! Наши специалисты скоро свяжутся с Вами по номеру телефона {phone}!"
        )
    return render(request, "contacts.html")


def product_detail(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context=context)
