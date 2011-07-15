from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pagination.paginator import InfinitePaginator

from ATP_Performance_Test.tuitter.models import Tuit

def show(request, id):
    try:
        shown_user = User.objects.get(pk=int(id))
    except User.DoesNotExist, ValueError:
        raise Http404

    recent_tuits = InfinitePaginator(Tuit.objects.select_related('user').filter(user=shown_user).order_by("-added"), 10).page(request.page)

    return render_to_response("profiles/show.html", {"shown_user": shown_user, "recent_tuits": recent_tuits}, context_instance=RequestContext(request))