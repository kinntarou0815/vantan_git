from django.http import HttpResponse

def helloworldfunc(request):
    return HttpResponse("hello,world")

def print_test(request):
    responseobject = HttpResponse("<h2>こんにちは</h2>")
    return responseobject


















