from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class Regester(View) :
    def get(self,request) :

        if request.user.is_authenticated == True :
            return redirect(reverse_lazy('home'))
        
        form = LoginForm()
        return render(request,'users/regester.html',{'form':form})
    
    def post(self,request) :
        form = LoginForm(request.POST)
        if (form.is_valid()) :
            form.save()
            messages.success(request,f'Account was created for: {request.POST['username']}')
            return redirect(reverse_lazy('login'))
        else :
            pass
        return render(request,'users/profile.html')
    
class Profile(LoginRequiredMixin,View) :
    def get(self,request) :
        return render(request,'users/profile.html')
    

class CoustomLoginView(LoginView) :
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request,f"Hello {self.request.POST['username']} You have been logged in successfully")
        return super().form_valid(form)
    

class CoustomLogoutView(LogoutView) :
    template_name = 'users/logout.html'
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request,f"You have successfully logged out")
        return super().dispatch(request, *args, **kwargs)
    
class ConfirmLogout(LoginRequiredMixin,View) :
    def get(self,request) :
        if request.user.is_authenticated :
            return render(request,'users/logout.html')
        else :
            return redirect(reverse_lazy('login'))