from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import networkx as nx
import time

from ATP_Performance_Test.tuitter.forms import AddTuitForm
from ATP_Performance_Test.tuitter.models import Tuit

@login_required
def add(request):
    if request.method == 'POST':
        form = AddTuitForm(request.POST)
        if form.is_valid():
            new_tuit = form.save(commit=False)
            new_tuit.user = request.user
            new_tuit.save()

            return HttpResponseRedirect(reverse('tuitter_show_tuit', args=[new_tuit.id]))
    else:
        form = AddTuitForm()

    return render_to_response("tuitter/add.html", {"form": form}, context_instance=RequestContext(request))

def show(request, id):
    try:
        tuit = Tuit.objects.select_related('user').get(pk=int(id))
    except Tuit.DoesNotExist, ValueError:
        raise Http404

    return render_to_response("tuitter/show.html", {"tuit": tuit}, context_instance=RequestContext(request))

def heatCPU(request):
    # simple example graph
    ts = time.time()
    G = nx.generators.classic.complete_graph(300)
    nx.algorithms.centrality.closeness_centrality(G)
    te = time.time()
    
    return HttpResponse("HeatCPU() time %.3f seconds" % (te-ts))



