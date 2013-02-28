from datetime import datetime

from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect

from bjj_log.drill_tracker.models import Drills

@login_required
def create(request):
    my_user = request.user
    if request.POST:
        post = request.POST
        name = post.get("name", None)
        start = post.get("start", None)
        end = post.get("end", None)
        link = post.get("link", None)
        total = post.get("total", None)
        if name is None or start is None or end is None \
        or total is None:
            error = "Must provide valid values for Name, Start Date, End Date and Total Reps"
            return render_to_response('create.html',
                                      {error},
                                       context_instance=RequestContext(request))
        else:
            drill = Drills()
            drill.name = name
            drill.sdate = datetime.strptime(start, "%m/%d/%Y")
            drill.edate = datetime.strptime(end, "%m/%d/%Y")
            drill.link = link
            drill.total = total
            drill.user = request.user
            drill.save()
            all_drills = my_user.drills.all()
            return render_to_response('check.html',
                                  {'all_drills':all_drills},
                                  context_instance=RequestContext(request))
    
    return render_to_response('create.html',
                              {},
                               context_instance=RequestContext(request))

@login_required
def check_or_update(request):
    my_user = request.user
    all_drills = my_user.drills.all()
    return render_to_response('check.html',
                              {'all_drills':all_drills},
                              context_instance=RequestContext(request))
    
    