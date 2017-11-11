from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog_app.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'

"""
If you want, you can indicat context_object_name fllow as blew

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'anthing as your wish'
"""


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_app/post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog_app/post_edit.html'



class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')

