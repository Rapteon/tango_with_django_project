from django.shortcuts import render
from django.http import HttpResponse


# This is just a single view. You can define additional views by adding
# more functions in this file. Each view requires a HttpRequest object
# as one argument and must return a HttpResponse object.
def index(request):
    # This dict is passed to the template engine to substitute "boldmessage" with the given text
    # in the template.
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}

    # The second argument is the path to the template inside the templates directory for rendering.
    return render(request, "rango/index.html", context=context_dict)


def about(request):
    context_dict = {"boldmessage": "This tutorial has been put together by Rapteon."}
    return render(request, "rango/about.html", context=context_dict)
