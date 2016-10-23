from django.shortcuts import render_to_response
from django.template import RequestContext
from members.models import Members
from members.forms import Memberform
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def all(request):
	try:
		if request.session['user']:
			return render_to_response('memlist.html',{'members':Members.objects.all()},context_instance=RequestContext(request))
	except:
		pass
		return render_to_response('memlist.html',{'message':"login Required to view"},context_instance=RequestContext(request))


def create(request):
	try:
		if request.session['user']:
			if request.POST:
				form = Memberform(request.POST)
				if form.is_valid():
					form.save()

					return HttpResponseRedirect('/members/all/')
			else:
				form = Memberform()
			args ={}
			args.update(csrf(request))
			args['form'] = form

			return render_to_response('memcreate.html',args,context_instance=RequestContext(request))
	except:
		pass
		return render_to_response('memcreate.html',{'message':"Contact librarian for Registration"},context_instance=RequestContext(request))


# Create your views here.
# if request.POST:
# 		form = Memberform(request.POST)
# 		if form.is_valid():
# 			form.save()

# 			HttpResponseRedirect('/members/all')
# 	else:
# 		form = Memberform()
# 	args ={}
# 	args.update(csrf(request))
# 	args['form'] = form

# 	return render_to_response('memcreate.html',args)