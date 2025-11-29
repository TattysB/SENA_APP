from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def aprendices(request):
  aprendices = Aprendiz.objects.all().values()
  template = loader.get_template('aprendices_list.html')
  context={
    'aprendices':aprendices,
  }
  return HttpResponse(template.render(context, request))

def detalle_aprendiz(request, aprendiz_id):
  aprendiz_detalle = Aprendiz.objects.get(id=aprendiz_id)
  template = loader.get_template('detalle_aprendiz.html')
  context={
    'aprendiz_detalle':aprendiz_detalle,
  }
  return HttpResponse(template.render(context, request))