from django.shortcuts import render, redirect, get_object_or_404#,reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, View, RedirectView,CreateView,UpdateView
from webapp.models import *
from django.urls import reverse_lazy
from webapp.forms import *
import datetime

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    def get_queryset(self):
         return Post.objects.all().order_by('date').reverse()

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    #form_class = PostForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('index')

def create_post_view(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'post_create.html')
        else:
            return redirect('login')

    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.user
        date = datetime.datetime.now()
        Post.objects.create(title=title, text=text, author=author,date=date)
        return redirect('index')

def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.user == post.author:
        if request.method == 'GET':
            return render(request, 'post_delete.html', context={
                'post': post
            })
        elif request.method == 'POST':
            if request.POST.get('delete') == 'yes':
                post.delete()
            return redirect('../')
    else:
        return redirect('../post/'+str(pk))

class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = UserInfo
    template_name = 'user_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('date').reverse()
        return context

class UserUpdateView(UpdateView):
    model = UserInfo
    fields = ['phone', 'image']
    #form_class = PostForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('index')
# Create your views here.
