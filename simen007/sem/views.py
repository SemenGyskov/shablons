from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    data = {"header": '8 908 910 37 79', "message": "VK: @SemGusb"}
    return render(request, "contacts.html", context=data)

def forms(request):
    return render(request, "forms.html")
