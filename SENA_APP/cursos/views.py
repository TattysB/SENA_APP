from django.shortcuts import render
from django.template import loader
from .models import Curso
from .forms import CursoForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def lista_cursos(request):

    cursos = Curso.objects.all()
    template = loader.get_template("lista_cursos.html")

    context = {
        "lista_cursos": cursos,
        "total_cursos": cursos.count(),
    }

    return HttpResponse(template.render(context, request))


def detalle_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    template = loader.get_template("detalle_curso.html")

    context = {
        "curso": curso,
        "aprendices_curso": aprendices_curso,
        "instructores_curso": instructores_curso,
    }

    return HttpResponse(template.render(context, request))


# CRUD VIEWS FOR CURSO


class CursoCreateView(generic.CreateView):
    """Vista para crear un nuevo curso"""

    model = Curso
    form_class = CursoForm
    template_name = "agregar_curso.html"
    success_url = reverse_lazy("cursos:lista_cursos")

    def form_valid(self, form):
        messages.success(
            self.request,
            f"El curso {form.instance.nombre} ha sido creado exitosamente.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        return super().form_invalid(form)


class CursoUpdateView(generic.UpdateView):
    """Vista para actualizar un curso existente"""

    model = Curso
    form_class = CursoForm
    template_name = "editar_curso.html"
    success_url = reverse_lazy("cursos:lista_cursos")
    pk_url_kwarg = "curso_id"

    def form_valid(self, form):
        messages.success(
            self.request,
            f"El curso {form.instance.nombre} ha sido actualizado exitosamente.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        return super().form_invalid(form)


class CursoDeleteView(generic.DeleteView):
    """Vista para eliminar un curso"""

    model = Curso
    template_name = "eliminar_curso.html"
    success_url = reverse_lazy("cursos:lista_cursos")
    pk_url_kwarg = "curso_id"

    def delete(self, request, *args, **kwargs):
        curso = self.get_object()
        messages.success(
            request, f"El curso {curso.nombre} ha sido eliminado exitosamente."
        )
        return super().delete(request, *args, **kwargs)
