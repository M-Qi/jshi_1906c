from django.http import HttpResponse

def dev(request):

    return HttpResponse('index')
