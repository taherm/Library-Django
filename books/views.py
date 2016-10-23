from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from books.models import Book
from books.forms import BookIssueForm
from django.http import HttpResponseRedirect

def all(request):
	try:
		if request.session['user']:
			args = {}
			args.update(csrf(request))
			args['books'] = Book.objects.all()
			return render_to_response('booklist.html',args,context_instance=RequestContext(request))
	except:
		pass
		return render_to_response('booklist.html',{'message':"login Required to view"},context_instance=RequestContext(request))

def search(request):
	if request.method=="POST":
		search_text = request.POST.get('search')
	else:
		search_text = ''

	books = Book.objects.filter(title__contains=search_text)

	return render_to_response('book_search.html',{'books':books})

def issue(request):
	try:
		if request.session['user']:
			if request.POST:
				form = BookIssueForm(request.POST)
				if form.is_valid():
					form.save()

					return HttpResponseRedirect('/books/issue/')
			else:
				form = BookIssueForm()
			args = {}
			args.update(csrf(request))
			args['form'] = form
			return render_to_response('issue.html',args,context_instance=RequestContext(request))
	except:
		pass
		return render_to_response('issue.html',{'message':"login required"},context_instance=RequestContext(request))



# Create your views here.
