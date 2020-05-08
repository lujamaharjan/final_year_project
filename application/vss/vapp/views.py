from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def encrypt(request):
    participants = [
        {"value": 3, "key": "Three"},
        {"value": 4, "key": "Four"},
        {"value": 5, "key": "Five"},
        {"value": 6, "key": "Six"},
        {"value": 7, "key": "Seven"},
        {"value": 8, "key": "Eight"},
        {"value": 9, "key": "Nine"}
    ]

    return render(request, 'encrypt.html', {'participants': participants})


def decrypt(request):
    return render(request, "decrypt.html")


def verify(request):
    return render(request, "verify.html")
