from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("aprendices/", views.aprendices, name="aprendices"),
    path("aprendices/aprendiz/<int:aprendiz_id>", views.detalle_aprendiz,name="detalle_aprendiz"),
]
