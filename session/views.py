from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from session.service import get_LgVacun

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


def vwVacunacion(request):
    if not request.user.is_authenticated:
        return render(request, "auth/login.html")
    else:
        return render(request, "contents/l_vacunacion.html")


def vacunacion(request):
    if request.method == "POST":
        cedula = request.POST["cedula"]
        nombres = request.POST["nombres"]
        params = {"cedula": cedula, "nombres": nombres}
        context = {"result": get_LgVacun(params)}
        return render(request, "contents/l_vacunacion.html", context)
