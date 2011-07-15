from django.http import HttpResponse
from django.shortcuts import render_to_response
from coffin.shortcuts import render_to_response as jinja_render_to_response
from django.template.context import RequestContext
from pagination.paginator import InfinitePaginator

from ATP_Performance_Test.tuitter.models import Tuit

def index(request):
    recent_tuits = InfinitePaginator(Tuit.objects.select_related('user').all().order_by("-added"), 10).page(request.page)

    return render_to_response("index.html", {"recent_tuits": recent_tuits}, context_instance=RequestContext(request))

def index_jinja2(request):
    recent_tuits = InfinitePaginator(Tuit.objects.select_related('user').all().order_by("-added"), 10).page(request.page)

    return jinja_render_to_response("index_jinja2.html", {"recent_tuits": recent_tuits}, context_instance=RequestContext(request))

def return_42(request):
    return HttpResponse('42')