from django.shortcuts import render
from . import forms
def StudentInputForm(request):
    form=forms.StudentForm()
    if request.method=='Post':
        form=forms.StudentForm(request.Post)
        if form.is_valid():
            print('Form validation success and printing the data')
            print('Name:', form.cleaned_data['name'])
            print('Rollno:', form.cleaned_data['rollno'])
            print('Marks:', form.cleaned_data['marks'])
    return render(request, 'app1/home.html',{'form':form})

# Create your views here.
