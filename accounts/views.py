from django.contrib import auth
from django.contrib.auth import logout
from accounts.forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

def register(request):
	'''
	For user registration
	'''
	logout(request) # logout firstly
	if request.method == 'POST':
		_form = UserRegistrationForm(request.POST)
		if _form.is_valid():
			new_user = _form.save()
			return HttpResponseRedirect('/')
	else:
		_form = UserRegistrationForm()

	context = {'form': _form}
	context.update(csrf(request))

	return render_to_response('register.html', context)

def auth_view(request):
	username =  request.POST.get('username', '')
	password =  request.POST.get('password', '')
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		request.session['user'] = username
		auth.login(request,user)
		return HttpResponseRedirect('/')
	else:
		messages.error(request,"INVALID LOGIN")
		return HttpResponseRedirect('/accounts/login/')

	


def home(request):
	'''
	lib-ms home page
	'''
	return render_to_response('base.html', {}, RequestContext(request))
# Create your views here.

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')