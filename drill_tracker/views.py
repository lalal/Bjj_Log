from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect


@login_required
def create(request):
    return render_to_response('create.html',
                              {},
                               context_instance=RequestContext(request))

@login_required
def check_or_update(request):
    pass