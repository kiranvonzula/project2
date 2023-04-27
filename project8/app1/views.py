from django.shortcuts import render
def home (request):
    return render(request,'app1/home.html')
def profile(request):
    return render(request,'app1/profile.html')
# Create your views here.
