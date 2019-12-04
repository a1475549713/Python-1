from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello world!this is my first web,it is so easy')

def heh (request):
    return HttpResponse('hahahah')