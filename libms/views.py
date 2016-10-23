from django.shortcuts import render_to_response
from django.template import RequestContext
def about(request):
	return render_to_response('about.html',context_instance=RequestContext(request))


