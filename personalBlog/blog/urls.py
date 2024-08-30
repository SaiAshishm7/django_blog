from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  # Home page for the blog
    path('post/<int:pk>/', views.post_view, name='post-detail'),
    path('post/new/', views.home, name='post-create'),
]
