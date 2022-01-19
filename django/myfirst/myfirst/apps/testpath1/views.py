from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, Django!")

def testnum1(request):
	return HttpResponse("Test page")