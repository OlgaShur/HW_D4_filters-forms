from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, ListView, DetailView, CreateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-post_time_create'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class PostListSearch(ListView):
    model = Post
    ordering = '-post_time_create'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 5
    filterset_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'one_news'

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
