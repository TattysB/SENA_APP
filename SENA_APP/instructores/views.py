from django.http import HttpResponse
from django.template import loader
from .models import Instructor


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def instructores(request):
    lista_instructores = Instructor.objects.all().values()
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
