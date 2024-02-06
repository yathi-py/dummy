from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import RegistrationForm


# Create your views here.

def home(request):
    return render(request,'home.html' )

class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request,self.template_name,{'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        return render(request,self.template_name,{'form':form})