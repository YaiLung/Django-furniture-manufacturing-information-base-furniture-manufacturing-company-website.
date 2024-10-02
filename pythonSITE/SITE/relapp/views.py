from django.shortcuts import render


def index(request):
    return render(request, 'relapp/index.html')

def about(request):
    return render(request,'relapp/' )

def help(request):

    return render(request,'relapp/' )
def what(request):
    return render(request,'relapp/' )