from django.shortcuts import render
from django.http import HttpResponse


# This is just a single view. You can define additional views by adding
# more functions in this file. Each view requires a HttpRequest object
# as one argument and must return a HttpResponse object.
def index(request):
    return HttpResponse("Rango says hey there partner!")
