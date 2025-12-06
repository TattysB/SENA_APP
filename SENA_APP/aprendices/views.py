from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz

from .forms import AprendizForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def aprendices(request):
    aprendices = Aprendiz.objects.all()
    template = loader.get_template("aprendices_list.html")
    context = {
        "aprendices": aprendices,
    }
    return HttpResponse(template.render(context, request))


def detalle_aprendiz(request, aprendiz_id):
    aprendiz_detalle = Aprendiz.objects.get(id=aprendiz_id)
    template = loader.get_template("detalle_aprendiz.html")
    context = {
        "aprendiz_detalle": aprendiz_detalle,
    }
    return HttpResponse(template.render(context, request))


# VISTAS BASADAS EN CLASES - CRUD APRENDIZ

# CREATE - APRENDIZ


class AprendizCreateView(generic.CreateView):
    """Vista para crear un nuevo aprendiz"""

    model = Aprendiz
    form_class = AprendizForm
    template_name = "agregar_aprendiz.html"
    success_url = reverse_lazy("aprendices:aprendices")

    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el aprendiz"""
        messages.success(
            self.request,
            f"El aprendiz {form.instance.nombre_completo()} ha sido registrado exitosamente.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        return super().form_invalid(form)


# UPDATE - APRENDIZ
class AprendizUpdateView(generic.UpdateView):
    """Vista para actualizar un aprendiz existente"""

    model = Aprendiz
    form_class = AprendizForm
    template_name = "editar_aprendiz.html"
    success_url = reverse_lazy("aprendices:aprendices")
    pk_url_kwarg = "aprendiz_id"

    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f"El aprendiz {form.instance.nombre_completo()} ha sido actualizado exitosamente.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        return super().form_invalid(form)


# DELETE - APRENDIZ
class AprendizDeleteView(generic.DeleteView):
    """Vista para eliminar un aprendiz"""

    model = Aprendiz
    template_name = "eliminar_aprendiz.html"
    success_url = reverse_lazy("aprendices:aprendices")
    pk_url_kwarg = "aprendiz_id"

    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        aprendiz = self.get_object()
        messages.success(
            request,
            f"El aprendiz {aprendiz.nombre_completo()} ha sido eliminado exitosamente.",
        )
        return super().delete(request, *args, **kwargs)
