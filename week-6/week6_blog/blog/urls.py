"""
Blog URL patterns (mounted at /posts/ from the root urls.py)

Demonstrates:
- Function-based view URLs
- Class-based view URLs (.as_view())
- URL parameters (<int:pk>)
"""

from django.urls import path
from . import views

urlpatterns = [
    # Lesson 11 – ListView
    path('', views.PostListView.as_view(), name='post_list'),

    # Lesson 11 – DetailView  (pk from URL → Post.pk)
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # Lesson 11 – CreateView  (protected by LoginRequiredMixin)
    path('create/', views.PostCreateView.as_view(), name='post_create'),

    # Lesson 11 – UpdateView  (protected; ownership checked in dispatch)
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),

    # Lesson 11 – DeleteView  (protected; ownership checked in dispatch)
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
