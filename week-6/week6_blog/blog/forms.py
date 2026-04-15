"""
Blog Forms – Week 6 Demo

Covers every form topic from the lesson:
  Lesson 2  – Plain Django Form (ContactForm) with all field types & widgets
  Lesson 3  – ModelForm (PostForm) with Meta options
  Lesson 4  – Custom field validation (clean_<fieldname>) and form-level clean()
  Lesson 9  – Custom UserCreationForm (RegisterForm)
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Post


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 4 – Custom standalone validator (reusable)
# ─────────────────────────────────────────────────────────────────────────────

def validate_no_spam(value):
    """Reject messages containing obvious spam keywords."""
    spam_words = ['buy now', 'click here', 'free money', 'winner']
    lower = value.lower()
    for word in spam_words:
        if word in lower:
            raise ValidationError(
                f'Your message contains a prohibited phrase: "{word}"'
            )


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 2 – Plain Django Form (not tied to a model)
# Demonstrates: all common field types, widgets, parameters
# ─────────────────────────────────────────────────────────────────────────────

class ContactForm(forms.Form):
    """
    A contact form that demonstrates:
    - Different field types (CharField, EmailField, ChoiceField, BooleanField)
    - Widget customisation (TextInput, Textarea, Select, CheckboxInput)
    - Field parameters: required, help_text, initial, label
    - Custom validator (validate_no_spam)
    - Field-level validation (clean_email)
    - Form-level validation (clean)
    """

    # Basic CharField with widget attributes
    name = forms.CharField(
        max_length=100,
        label='Your Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'John Smith',
        }),
    )

    # EmailField – built-in email format validation
    email = forms.EmailField(
        help_text="We'll never share your email with anyone.",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com',
        }),
    )

    # Optional field (required=False)
    phone = forms.CharField(
        required=False,
        label='Phone (optional)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+1 555 000 0000',
        }),
    )

    # ChoiceField – renders as <select>
    SUBJECT_CHOICES = [
        ('',         '— Select a subject —'),
        ('general',  'General Inquiry'),
        ('support',  'Technical Support'),
        ('feedback', 'Feedback'),
        ('other',    'Other'),
    ]
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    # CharField with Textarea widget + custom validator
    message = forms.CharField(
        label='Your Message',
        validators=[validate_no_spam],
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Write your message here…',
        }),
    )

    # BooleanField – renders as checkbox
    subscribe = forms.BooleanField(
        required=False,
        label='Subscribe to our newsletter',
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    # ─── Lesson 4: Field-level validation ────────────────────────────────────
    def clean_email(self):
        """Reject disposable email domains."""
        email = self.cleaned_data.get('email', '')
        blocked_domains = ['mailinator.com', 'tempmail.com', 'throwaway.email']
        domain = email.split('@')[-1].lower()
        if domain in blocked_domains:
            raise forms.ValidationError(
                f'Email addresses from "{domain}" are not accepted.'
            )
        return email

    # ─── Lesson 4: Form-level validation (cross-field) ───────────────────────
    def clean(self):
        """Require phone number when subject is 'support'."""
        cleaned_data = super().clean()
        subject = cleaned_data.get('subject')
        phone   = cleaned_data.get('phone')

        if subject == 'support' and not phone:
            raise forms.ValidationError(
                'Please provide a phone number for technical support requests '
                'so we can call you back.'
            )
        return cleaned_data


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 3 – ModelForm
# Automatically generates fields from the Post model
# ─────────────────────────────────────────────────────────────────────────────

class PostForm(forms.ModelForm):
    """
    ModelForm for creating and editing blog posts.

    Demonstrates:
    - fields (explicit whitelist)
    - labels override
    - help_texts
    - widgets with custom attributes
    - ModelForm field-level validation (clean_title)
    """

    class Meta:
        model  = Post
        fields = ['title', 'content', 'status']   # explicit whitelist (safer than '__all__')

        labels = {
            'title':   'Post Title',
            'content': 'Post Content',
            'status':  'Visibility',
        }

        help_texts = {
            'status': 'Draft posts are only visible to you; published posts are public.',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a clear, descriptive title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post here…',
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    # Lesson 4: field-level validation on a ModelForm
    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        if title.lower() == title:
            raise forms.ValidationError('Title should start with a capital letter.')
        return title


# ─────────────────────────────────────────────────────────────────────────────
# Lesson 9 – Custom Registration Form (extends UserCreationForm)
# ─────────────────────────────────────────────────────────────────────────────

class RegisterForm(UserCreationForm):
    """
    Extends Django's built-in UserCreationForm to add:
    - email (required)
    - first_name, last_name

    Demonstrates:
    - Extending built-in forms
    - Custom clean_username (field-level validation)
    - Bootstrap widget attributes
    """

    email = forms.EmailField(
        required=True,
        help_text='Required. Enter a valid email address.',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
    )

    class Meta:
        model  = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap classes to the inherited password fields
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    # Lesson 4: clean_<fieldname> – field-level validation
    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        if ' ' in username:
            raise forms.ValidationError('Username cannot contain spaces.')

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('That username is already taken.')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('An account with that email already exists.')
        return email
