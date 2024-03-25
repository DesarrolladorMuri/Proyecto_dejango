from django.http import HttpResponse
from django.template import Template,Context, loader

def index (request):
    pgHtml = loader.get_template('index.html')
    documento = pgHtml.render({})
    return HttpResponse (documento)