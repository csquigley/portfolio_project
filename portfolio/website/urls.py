from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('posts/',views.PostListView.as_view(),name='posts'),
    path('projects/',views.ProjectListView.as_view(),name='projects'),
    path('project/<int:pk>/',views.ProjectDetailView.as_view(),name='project_detail'),
    path('contact/',views.ContactView.as_view(),name='contact'),
]
