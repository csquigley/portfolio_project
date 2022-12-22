from django.shortcuts import render, reverse
from django.views.generic import ListView, TemplateView, DetailView
from .models import Post, Projects

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        context['page'] = 'home'
        return context

class PostListView(ListView):
    model = Post
    template_name = 'posts.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request        
        context['page'] = 'posts'
        return context

class ProjectListView(ListView):
    model = Projects
    template_name='projects.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request        
        context['page'] = 'projects'
        return context

class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'project_detail.html'


