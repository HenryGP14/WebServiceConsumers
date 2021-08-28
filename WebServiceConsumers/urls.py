from django.contrib import admin
from django.urls import path, include

from session import views as views_global
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("login/", views_global.vwLogin, name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
    path("", views_global.vwHome, name="index"),
    path("poblacion", views_global.vwPais, name="poblacion"),
    path("vacunacion", views_global.vwVacunacion, name="vacunacion"),
    path("vacunacion/consular", views_global.vacunacion, name="consulta"),
    path("sport", views_global.vwSport, name="sport"),
]
