from django.shortcuts import render

# Create your views here.


def customform(request):

    return render(request,'form.html')