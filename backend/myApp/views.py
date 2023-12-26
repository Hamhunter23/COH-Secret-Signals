from django.shortcuts import render
from myApp.models import Test


# Create your views here.

def index(request):
    if request.method == "POST":
        file = request.POST.get('upload')
        test = Test(file=file)
        test.save()
    return render(request,'index.html')