from django.shortcuts import render
from.models import Places8
# Create your views here.
def demo(request):
    obj = Places8.objects.all()
    return render(request,"index.html",{'result':obj})