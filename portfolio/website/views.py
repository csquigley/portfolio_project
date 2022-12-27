from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, TemplateView, DetailView, FormView
from .models import Post, Project, ProjectSection
from .forms import ContactForm


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

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class ProjectListView(ListView):
    model = Project
    template_name='projects.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request        
        context['page'] = 'projects'
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['sections'] = ProjectSection.objects.filter(project=self.object.id)  
        context['page'] = 'project'
        return context

class ContactView(FormView):    
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request        
        context['page'] = 'contact'
        return context

    def form_valid(self, form):
        # Send the email
        send_mail(
            'Contact Form Submission',
            form.cleaned_data['message'],
            form.cleaned_data['email'],
            ['recipient@example.com'],
            fail_silently=False,
        )
        
        # Render the confirmation template
        return render(self.request, 'contact/confirmation.html')



