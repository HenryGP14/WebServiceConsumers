from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
@login_required
def vwHome(request):
    return render(request, "index.html")


def vwLogin(request):
    if not request.user.is_authenticated:
        return render(request, "auth/login.html")
    else:
        return redirect("index")


def vwPais(request):
    if not request.user.is_authenticated:
        return render(request, "auth/login.html")
    else:
        return render(request, "contents/list_pais.html")
