from django.shortcuts import render
# import os
# Create your views here.
def index(request):
    # print(os.getcwd())
    return render(request, "reader/index.html")
