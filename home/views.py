from django.shortcuts import get_object_or_404, render
from django.urls import reverse,reverse_lazy
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# All Posts
class Home(ListView) :
    model = Post
    template_name = 'blog/home.html'
    field = ['title']
    
# Details Post
class Details_Post(View) :
    def get(self,request,pk) :
        cxt = {
            'post' : get_object_or_404(Post,pk = pk),
        }
        return render(request , 'blog/post_details.html' , cxt)

# Create Post
class PostCreate(LoginRequiredMixin,CreateView) :
    model = Post
    template_name = "blog/post_form.html"
    fields = ['title','content']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        # or we can use
        # object = form.save(commit=False)
        # object.owner = self.request.user
        # object.save()
        
        return super().form_valid(form)

# Update Post
class PostUpdate(LoginRequiredMixin,UpdateView) :
    model = Post
    template_name = "blog/post_form.html"
    fields = ['title' , 'content']
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        q = super().get_queryset()
        return q.filter(owner = self.request.user)
    
    

# Delete Post
class PostDelete(LoginRequiredMixin,DeleteView) :
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        q = super().get_queryset()
        return q.filter(owner = self.request.user)
