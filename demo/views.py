from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def home(request):
    return render(request, 'index.html')

@api_view()
def api(request):
    return Response("sending data to frontend")