from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pagination.paginator import InfinitePaginator

from ATP_Performance_Test.tuitter.models import Tuit

def index(request):
    recent_tuits = InfinitePaginator(Tuit.objects.all(), 10).page(request.page)

    return render_to_response("index.html", {"recent_tuits": recent_tuits}, context_instance=RequestContext(request))