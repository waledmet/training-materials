"""
Root URL Configuration
Week 6 Demo: Forms, Validation & Authentication
"""

from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home page
    path('', blog_views.home_view, name='home'),

    # Contact form (Lesson 2: Plain Django Form)
    path('contact/', blog_views.contact_view, name='contact'),
    path('contact/success/', blog_views.contact_success_view, name='contact_success'),

    # Authentication (Lessons 7, 8, 9)
    path('register/', blog_views.register_view, name='register'),
    path('login/', blog_views.login_view, name='login'),
    path('logout/', blog_views.logout_view, name='logout'),

    # User dashboard (Lesson 10: @login_required)
    path('dashboard/', blog_views.dashboard_view, name='dashboard'),

    # Blog posts – mix of function-based and class-based views
    path('posts/', include('blog.urls')),
]
