from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page


# This is just a single view. You can define additional views by adding
# more functions in this file. Each view requires a HttpRequest object
# as one argument and must return a HttpResponse object.
def index(request):
    # Get first five categories order by number of likes in descending order
    # (category with highest likes followed by ones with lower likes)
    # Note: The `-` (minus) denotes descending order. Without it, the results
    # will be ordered in ascending order.
    category_list = Category.objects.order_by("-likes")[:5]

    # This dict is passed to the template engine to substitute "boldmessage" with the given text
    # in the template.
    context_dict = {}
    context_dict["boldmessage"] = "Crunchy, creamy, cookie, candy, cupcake!"
    context_dict["categories"] = category_list

    # The second argument is the path to the template inside the templates directory for rendering.
    return render(request, "rango/index.html", context=context_dict)


def about(request):
    context_dict = {"boldmessage": "This tutorial has been put together by Rapteon."}
    return render(request, "rango/about.html", context=context_dict)


def show_category(request, category_name_slug):
    # For passing to template rendering engine.
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict["pages"] = pages
        context_dict["category"] = category

    except Category.DoesNotExist:
        context_dict["pages"] = None
        context_dict["category"] = None

    return render(request, "rango/category.html", context=context_dict)
