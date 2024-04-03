from django.shortcuts import render
# from django.http import HttpResponse
# from .models import gereradorGrafico
# import matplotlib.pyplot as plt
# import io
# import urllib, base64

# Create your views here.
def home(request):
    return render(request, 'index.html')