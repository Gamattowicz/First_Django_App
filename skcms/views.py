from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from notifications.models import Notifications

class Login(View):
    def get(self, request):
        context = {}
        context.update(csrf(request))
        return render(request, 'login.html', context)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
	n = Notifications.objects.filter(user = request.user, viewed = False)
	return render(request, 'loggedin.html',{'user_name' : request.user.username, 'notification': n})

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def invalid_login(request):
    return render(request, 'invalid_login.html')

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/create_user_success/')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()

    return render(request, 'create_user.html', args)

def create_user_success(request):
    return render(request, 'create_user_success.html')