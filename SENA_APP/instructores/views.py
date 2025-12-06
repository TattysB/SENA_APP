from django.http import HttpResponse
from django.template import loader
from .models import Instructor
from .forms import InstructorForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def instructores(request):
    lista_instructores = Instructor.objects.all()
    template = loader.get_template("lista_instructores.html")
    context = {
        "lista_instructores": lista_instructores,
    }
    return HttpResponse(template.render(context, request))


def detalle_instructor(request, instructor_id):
    instructor_detalle = Instructor.objects.get(id=instructor_id)
    template = loader.get_template("instructor_detalle.html")
    context = {
        "instructor_detalle": instructor_detalle,
    }
    return HttpResponse(template.render(context, request))


# CRUD VIEWS FOR INSTRUCTOR


class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo instructor"""

    model = Instructor
    form_class = InstructorForm
    template_name = "agregar_instructor.html"
    success_url = reverse_lazy("instructores:lista_instructores")

    def form_valid(self, form):
        messages.success(
            self.request,
            f"El instructor {form.instance.nombre} ha sido creado exitosamente.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        return super().form_invalid(form)


class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar un instructor existente"""

    model = Instructor
    form_class = InstructorForm
    template_name = "editar_instructor.html"
    success_url = reverse_lazy("instructores:lista_instructores")
    pk_url_kwarg = "instructor_id"

    def form_valid(self, form):
        messages.success(
            self.request,
            f"El instructor {form.instance.nombre} ha sido actualizado exitosamente.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        return super().form_invalid(form)


class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un instructor"""

    model = Instructor
    template_name = "eliminar_instructor.html"
    success_url = reverse_lazy("instructores:lista_instructores")
    pk_url_kwarg = "instructor_id"

    def delete(self, request, *args, **kwargs):
        instructor = self.get_object()
        messages.success(
            request,
            f"El instructor {instructor.nombre} ha sido eliminado exitosamente.",
        )
        return super().delete(request, *args, **kwargs)
