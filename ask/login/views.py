from django.http import HttpResponse


def login(request):
    return HttpResponse("This is login!")


