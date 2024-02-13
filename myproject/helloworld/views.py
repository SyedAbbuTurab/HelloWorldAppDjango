from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})


def hello_world_html(request):
    return render(request, 'hello_world.html')
