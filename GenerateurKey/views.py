from django.shortcuts import render
import secrets

def generate_secret_key(request):
    secret_key = secrets.token_hex(24)
    return render(request, 'index.html', {'secret_key': secret_key})

def about(request):
    return render(request, 'about.html')