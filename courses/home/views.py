from django.shortcuts import render
from django.contrib import messages


def index(request):
    messages.success(request, 'Успешно!')
    # return HttpResponse("What's up?")
    return render(request, 'home/index.html')

def pricing(request):

    # return HttpResponse("What's up?")
    return render(request, 'home/pricing.html')


