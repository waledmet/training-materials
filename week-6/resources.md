# Week 6 Resources – Forms, Validation & Authentication

Curated learning resources for Week 6 topics.

---

## Official Django Documentation

### Essential Reading

1. **Django Forms** - https://docs.djangoproject.com/en/stable/topics/forms/
2. **Form and Field Validation** - https://docs.djangoproject.com/en/stable/ref/forms/validation/
3. **User Authentication** - https://docs.djangoproject.com/en/stable/topics/auth/
4. **Class-Based Views** - https://docs.djangoproject.com/en/stable/topics/class-based-views/
5. **Messages Framework** - https://docs.djangoproject.com/en/stable/ref/contrib/messages/

---

## Video Tutorials

**Corey Schafer - Django Forms & Auth**
- Django Form tutorials
- User authentication series
- Level: Beginner-friendly

**Tech with Tim - Django Authentication**
- Complete auth tutorial
- Real-world examples
- Level: Beginner

---

## Cheat Sheets

### Form Fields Quick Reference

```python
# Text Fields
CharField()
EmailField()
URLField()
IntegerField()
DecimalField()
BooleanField()
DateField()
DateTimeField()
ChoiceField()
FileField()
ImageField()

# Common Parameters
required=True/False
max_length=100
min_value=0, max_value=100
initial='default'
help_text='Help text'
widget=forms.Textarea
```

### Form Validation Methods

```python
# Field-specific validation
def clean_<fieldname>(self):
    data = self.cleaned_data.get('<fieldname>')
    # Validate data
    return data

# Form-level validation
def clean(self):
    cleaned_data = super().clean()
    # Cross-field validation
    return cleaned_data
```

### Authentication Quick Reference

```python
# Create user
User.objects.create_user(username, email, password)

# Authenticate
user = authenticate(request, username=u, password=p)

# Login
login(request, user)

# Logout
logout(request)

# Check if authenticated
if user.is_authenticated:
    pass

# Protect views
@login_required
def my_view(request):
    pass
```

### Class-Based Views

```python
# ListView
from django.views.generic import ListView
class MyListView(ListView):
    model = MyModel
    template_name = 'list.html'
    context_object_name = 'items'

# DetailView
class MyDetailView(DetailView):
    model = MyModel
    template_name = 'detail.html'

# CreateView
class MyCreateView(CreateView):
    model = MyModel
    form_class = MyForm
    template_name = 'form.html'
    success_url = reverse_lazy('list')

# UpdateView
class MyUpdateView(UpdateView):
    model = MyModel
    form_class = MyForm
    template_name = 'form.html'

# DeleteView
class MyDeleteView(DeleteView):
    model = MyModel
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('list')

# With authentication
from django.contrib.auth.mixins import LoginRequiredMixin
class MyView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
```

---

## Practice Projects

### Build These for Practice

**1. Contact Form App**
- Contact form
- Email validation
- Success page

**2. User Management**
- Registration
- Login/logout
- Profile page
- Edit profile

**3. To-Do App with Auth**
- User registration
- Personal task lists
- CRUD operations
- Only see own tasks

**4. Blog with Comments**
- Post CRUD
- User authentication
- Comment system
- Edit own posts/comments

---

## Common Patterns

### Form Processing Pattern

```python
def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process data
            form.save()
            messages.success(request, 'Success!')
            return redirect('success')
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})
```

### ModelForm Edit Pattern

```python
def edit_view(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)

    if request.method == 'POST':
        form = MyForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
    else:
        form = MyForm(instance=obj)

    return render(request, 'form.html', {'form': form})
```

---

## Security Best Practices

**Forms:**
- Always use `{% csrf_token %}`
- Validate all input server-side
- Use `cleaned_data` not `request.POST` directly
- Sanitize user input

**Authentication:**
- Never store plain passwords
- Use `create_user()` and `set_password()`
- Use `@login_required` decorator
- Check object ownership before edit/delete
- Use HTTPS in production

**General:**
- Don't trust user input
- Validate everything
- Use Django's built-in protection
- Keep Django updated

---

## Additional Resources

- Real Python Django tutorials
- Django Girls Tutorial
- Simple is Better than Complex blog
- Two Scoops of Django (book)

---

**Remember:** Practice is key. Build projects and experiment!
