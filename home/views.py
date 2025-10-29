from django.shortcuts import get_object_or_404, render
from django.urls import reverse,reverse_lazy
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import Post

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
class PostCreate(CreateView) :
    model = Post
    template_name = "blog/post_form.html"
    fields = ['title','content']
    success_url = reverse_lazy('home')

# Update Post
class PostUpdate(UpdateView) :
    model = Post
    template_name = "blog/post_form.html"
    fields = ['title' , 'content']
    success_url = reverse_lazy('home')

# Delete Post
class PostDelete(DeleteView) :
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('home')
