# from django.shortcuts import render
#
# from django.shortcuts import render, HttpResponse
# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")


from django.shortcuts import render
from time import gmtime, strftime


def index(request):
    context = {
        "time_display": strftime("%Y-%m-%d %H:%M %p", gmtime())

    }
    return render(request, 'index.html', context)



# Create your views here.
