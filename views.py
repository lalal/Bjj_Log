from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from bjj_log.forms import UserCreateForm

@login_required
def base(request):
    return render(request, 'base.html')


def logout(request):
    try:
        auth.logout(request)
    except:
        pass
    return redirect('/')


def register(request):
    user = request.user
    if user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            auth.logout(request)
            user = form.save()
            if user is not None:
                user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'])
                auth.login(request, user)
                return redirect('/')
    else:
        form = UserCreateForm()
    return render_to_response('register.html',
                              {'form':form},
                              context_instance=RequestContext(request))


def login(request):
    user = request.user
    if user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return redirect('/')
    else:
        form = AuthenticationForm()
    request.session.set_test_cookie()

    return render_to_response('login.html',
                              {'form':form},
                              context_instance=RequestContext(request))
