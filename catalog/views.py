from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"Спасибо, {name}, за Ваше сообщение! Наши специалисты скоро свяжутся с Вами по номеру телефона {phone}!"
        )
    return render(request, "contacts.html")
