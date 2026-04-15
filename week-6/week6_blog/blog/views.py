"""
Blog Views – Week 6 Demo

Demonstrates BOTH view styles from the lesson:

Function-Based Views (FBV):
  home_view          – simple page
  contact_view       – Lesson 2/4/5: plain Form, GET/POST, validation
  contact_success_view
  login_view         – Lesson 8: authenticate() + login()
  logout_view        – Lesson 8: logout()
  register_view      – Lesson 9: UserCreationForm
  dashboard_view     – Lesson 10: @login_required

Class-Based Views (CBV)  – Lesson 11:
  PostListView       – ListView
  PostDetailView     – DetailView
  PostCreateView     – CreateView  + LoginRequiredMixin
  PostUpdateView     – UpdateView  + LoginRequiredMixin + ownership check
  PostDeleteView     – DeleteView  + LoginRequiredMixin + ownership check
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required          # Lesson 10
from django.contrib.auth.mixins import LoginRequiredMixin          # Lesson 11
from django.contrib import messages                                 # Lesson 12
from django.views.generic import (                                 # Lesson 11
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy

from .models import Post
from .forms import ContactForm, PostForm, RegisterForm


# ═════════════════════════════════════════════════════════════════════════════
# Home page
# ═════════════════════════════════════════════════════════════════════════════

def home_view(request):
    """Landing page – shows recent published posts and lesson overview."""
    recent_posts = Post.objects.filter(status=Post.STATUS_PUBLISHED)[:3]
    return render(request, 'home.html', {'recent_posts': recent_posts})


# ═════════════════════════════════════════════════════════════════════════════
# Lesson 2 / 4 / 5 – Contact Form (plain Form, not ModelForm)
# Demonstrates: GET/POST pattern, form validation, cleaned_data
# ═════════════════════════════════════════════════════════════════════════════

def contact_view(request):
    """
    GET  → display empty ContactForm
    POST → validate; on success redirect; on error re-render with errors
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)          # Bind submitted data

        if form.is_valid():
            # Access cleaned (validated) data
            name    = form.cleaned_data['name']
            email   = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            # (In a real app you would send an email here)

            messages.success(
                request,
                f"Thanks {name}! We received your message and will reply to {email}."
            )
            return redirect('contact_success')

        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = ContactForm()   # Unbound (empty) form for GET

    return render(request, 'contact.html', {'form': form})


def contact_success_view(request):
    return render(request, 'contact_success.html')


# ═════════════════════════════════════════════════════════════════════════════
# Lesson 7 / 8 – Authentication: Login & Logout
# ═════════════════════════════════════════════════════════════════════════════

def login_view(request):
    """
    Manual login using authenticate() + login().
    Demonstrates: authenticate(), login(), request.user, messages
    """
    if request.user.is_authenticated:
        return redirect('post_list')   # Already logged in

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # authenticate() checks credentials and returns User or None
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # Creates the session
            messages.success(request, f'Welcome back, {user.username}!')

            # Honour ?next= redirect (e.g. from @login_required)
            next_url = request.GET.get('next', 'post_list')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'registration/login.html')


def logout_view(request):
    """
    POST-only logout (best practice: use a form, not a link).
    Demonstrates: logout(), messages.info
    """
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been logged out.')
    return redirect('home')


# ═════════════════════════════════════════════════════════════════════════════
# Lesson 9 – User Registration
# ═════════════════════════════════════════════════════════════════════════════

def register_view(request):
    """
    Register a new user using our custom RegisterForm (extends UserCreationForm).
    Demonstrates: UserCreationForm, form.save(), auto-login after registration
    """
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name', '')
            user.last_name  = form.cleaned_data.get('last_name', '')
            user.save()

            # Auto-login after registration
            login(request, user)
            messages.success(
                request,
                f"Welcome to the blog, {user.username}! Your account has been created."
            )
            return redirect('post_list')

        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


# ═════════════════════════════════════════════════════════════════════════════
# Lesson 10 – Protecting Views with @login_required
# ═════════════════════════════════════════════════════════════════════════════

@login_required   # Redirects to LOGIN_URL if not authenticated
def dashboard_view(request):
    """
    User's personal dashboard.
    Demonstrates: @login_required, request.user, filtering by author
    """
    user_posts = Post.objects.filter(author=request.user)
    published  = user_posts.filter(status=Post.STATUS_PUBLISHED)
    drafts     = user_posts.filter(status=Post.STATUS_DRAFT)

    context = {
        'user_posts': user_posts,
        'published':  published,
        'drafts':     drafts,
    }
    return render(request, 'blog/dashboard.html', context)


# ═════════════════════════════════════════════════════════════════════════════
# Lesson 11 – Class-Based Views
# ═════════════════════════════════════════════════════════════════════════════

class PostListView(ListView):
    """
    ListView – display all published posts.
    Lesson 11: model, template_name, context_object_name, ordering, paginate_by
    """
    model                = Post
    template_name        = 'blog/post_list.html'
    context_object_name  = 'posts'
    paginate_by          = 5   # Built-in pagination

    def get_queryset(self):
        """Only show published posts to the public listing."""
        return Post.objects.filter(status=Post.STATUS_PUBLISHED)


class PostDetailView(DetailView):
    """
    DetailView – display a single post by primary key.
    Lesson 11: looks up by pk from the URL automatically.
    """
    model               = Post
    template_name       = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    CreateView – form to create a new post.
    Lesson 11: form_class, success_url, form_valid override to set author
    Lesson 10: LoginRequiredMixin instead of @login_required
    """
    model        = Post
    form_class   = PostForm
    template_name = 'blog/post_form.html'
    success_url  = reverse_lazy('post_list')
    login_url    = '/login/'

    def form_valid(self, form):
        """Set the post author to the current user before saving."""
        form.instance.author = self.request.user           # commit=False equivalent
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create New Post'
        context['submit_label'] = 'Publish Post'
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    UpdateView – form to edit an existing post.
    Lesson 10/11: ownership check in get_object(), LoginRequiredMixin
    """
    model        = Post
    form_class   = PostForm
    template_name = 'blog/post_form.html'
    login_url    = '/login/'

    def get_object(self, queryset=None):
        """Fetch the post and verify the current user is the author."""
        post = super().get_object(queryset)
        if post.author != self.request.user:
            messages.error(self.request, 'You can only edit your own posts.')
            # Raise PermissionDenied or redirect – we redirect via dispatch
        return post

    def dispatch(self, request, *args, **kwargs):
        """Redirect non-owners before the view processes the request."""
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=kwargs['pk'])
            if post.author != request.user:
                messages.error(request, 'You can only edit your own posts.')
                return redirect('post_detail', pk=post.pk)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Post updated successfully!')
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title']   = 'Edit Post'
        context['submit_label'] = 'Save Changes'
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    DeleteView – confirm and delete a post.
    Lesson 11: uses a confirmation template.
    """
    model        = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url  = reverse_lazy('post_list')
    login_url    = '/login/'

    def dispatch(self, request, *args, **kwargs):
        """Only the post author may delete."""
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=kwargs['pk'])
            if post.author != request.user:
                messages.error(request, 'You can only delete your own posts.')
                return redirect('post_detail', pk=post.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Post deleted.')
        return super().form_valid(form)
