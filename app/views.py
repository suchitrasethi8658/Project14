from django.shortcuts import render

# Create your views here.
def bootstrap5(request):
    return render(request,'bootstrap5.html')

def child(request):
    return render(request,'child.html')

