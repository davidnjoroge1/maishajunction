from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def pay(request):
    return render(request, 'home/pay.html')