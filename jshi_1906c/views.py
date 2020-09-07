from django.http import HttpResponse

def dev(request):

    return HttpResponse('index')


def dev2(request):
    return HttpResponse('index2')
