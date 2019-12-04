from django.http import HttpResponse



def do_admin(r):
    return HttpResponse('i am luyinbin ')

def do_param(r,pn):
    return HttpResponse('the namber is {}'.format(pn))

def do_name(r,name):
    return HttpResponse("my name is {}".format(name))