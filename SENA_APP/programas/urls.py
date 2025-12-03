from django.urls import path
from . import views

urlpatterns = [
    path("", views.programas, name="programas"),
    path(
        "programa/<int:programa_id>/", views.detalle_programa, name="detalle_programa"
    ),
]
