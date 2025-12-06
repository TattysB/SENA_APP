from django.http import HttpResponse
from django.template import loader
from .models import Programa
from .forms import ProgramaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template("lista_programas.html")
    context = {
        "programas": lista_programas,
        "total_programas": lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))


def detalle_programa(request, programa_id):
    programa_detalle = Programa.objects.get(id=programa_id)
    template = loader.get_template("programa_detalle.html")
    context = {
        "programa_detalle": programa_detalle,
    }
    return HttpResponse(template.render(context, request))


# CRUD VIEWS FOR PROGRAMA


class ProgramaCreateView(generic.CreateView):
    """Vista para crear un nuevo programa"""

    model = Programa
    form_class = ProgramaForm
    template_name = "agregar_programa.html"
    success_url = reverse_lazy("programas:programas")

    def form_valid(self, form):
        messages.success(
            self.request,
            f"El programa {form.instance.nombre} ha sido creado exitosamente.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        return super().form_invalid(form)


class ProgramaUpdateView(generic.UpdateView):
    """Vista para actualizar un programa existente"""

    model = Programa
    form_class = ProgramaForm
    template_name = "editar_programa.html"
    success_url = reverse_lazy("programas:programas")
    pk_url_kwarg = "programa_id"

    def form_valid(self, form):
        messages.success(
            self.request,
            f"El programa {form.instance.nombre} ha sido actualizado exitosamente.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        return super().form_invalid(form)


class ProgramaDeleteView(generic.DeleteView):
    """Vista para eliminar un programa"""

    model = Programa
    template_name = "eliminar_programa.html"
    success_url = reverse_lazy("programas:programas")
    pk_url_kwarg = "programa_id"

    def delete(self, request, *args, **kwargs):
        programa = self.get_object()
        messages.success(
            request, f"El programa {programa.nombre} ha sido eliminado exitosamente."
        )
        return super().delete(request, *args, **kwargs)
