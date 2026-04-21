# Week 7 Resources – APIs, JavaScript & Django REST Framework

Curated learning resources for Week 7 topics.

---

## Official Documentation

### Essential Reading

1. **Django REST Framework** - https://www.django-rest-framework.org/
2. **DRF Tutorial** - https://www.django-rest-framework.org/tutorial/quickstart/
3. **DRF Serializers** - https://www.django-rest-framework.org/api-guide/serializers/
4. **DRF ViewSets** - https://www.django-rest-framework.org/api-guide/viewsets/
5. **MDN JavaScript Guide** - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
6. **MDN Fetch API** - https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

---

## Video Tutorials

**Corey Schafer - Django REST Framework**
- Complete DRF tutorial series
- Well-explained concepts
- Level: Beginner-friendly

**Traversy Media - JavaScript Crash Course**
- Modern JavaScript basics
- ES6+ features
- Level: Beginner

**Tech with Tim - REST API Tutorial**
- Building APIs with Django
- Practical examples
- Level: Beginner

---

## Cheat Sheets

### REST API Quick Reference

```
HTTP Methods:
GET     - Read/retrieve
POST    - Create new
PUT     - Update (full)
PATCH   - Update (partial)
DELETE  - Remove

Status Codes:
200 OK              - Success
201 Created         - Resource created
204 No Content      - Deleted
400 Bad Request     - Invalid input
401 Unauthorized    - Not logged in
403 Forbidden       - No permission
404 Not Found       - Doesn't exist
500 Server Error    - Bug/crash
```

### DRF Serializers

```python
# Basic Serializer
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()

# ModelSerializer (recommended)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']
        # Or: fields = '__all__'

# Custom field
excerpt = serializers.SerializerMethodField()

def get_excerpt(self, obj):
    return obj.content[:100]

# Validation
def validate_title(self, value):
    if len(value) < 5:
        raise serializers.ValidationError("Too short")
    return value
```

### DRF Views

```python
# Function-based
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)

# Class-based
class PostList(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)

# Generic views
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### DRF Routers

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### JavaScript Basics

```javascript
// Variables
let name = 'Ahmed';      // Can reassign
const age = 25;          // Cannot reassign

// Functions
function greet(name) {
    return 'Hello, ' + name;
}

// Arrow function
const greet = (name) => 'Hello, ' + name;

// Arrays
const items = [1, 2, 3];
items.push(4);
items.forEach(item => console.log(item));
items.map(item => item * 2);
items.filter(item => item > 2);

// Objects
const person = {
    name: 'Ahmed',
    age: 25
};
console.log(person.name);

// Template literals
const msg = `Hello, ${name}! You are ${age}.`;
```

### Fetch API

```javascript
// GET request
fetch('/api/posts/')
    .then(response => response.json())
    .then(data => console.log(data));

// Async/await
async function getPosts() {
    const response = await fetch('/api/posts/');
    const data = await response.json();
    return data;
}

// POST request
fetch('/api/posts/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
        title: 'New Post',
        content: 'Content here'
    })
});

// DELETE request
fetch('/api/posts/1/', {
    method: 'DELETE',
    headers: {
        'X-CSRFToken': csrftoken
    }
});
```

### DOM Manipulation

```javascript
// Select elements
document.getElementById('id');
document.querySelector('.class');
document.querySelectorAll('div');

// Change content
element.textContent = 'Text';
element.innerHTML = '<b>HTML</b>';

// Create elements
const div = document.createElement('div');
div.textContent = 'New!';
container.appendChild(div);

// Events
button.addEventListener('click', () => {
    console.log('Clicked!');
});

// Page load
document.addEventListener('DOMContentLoaded', () => {
    // Page ready
});
```

---

## Practice Projects

### Build These for Practice

**1. Simple API**
- Create JSON endpoints manually
- Return list and detail views
- Handle errors

**2. Blog API with DRF**
- Post model with serializer
- Full CRUD ViewSet
- Browsable API

**3. JavaScript Posts Viewer**
- Fetch posts from API
- Display in cards
- Add loading state

**4. Task Manager (Week Project)**
- Task API with toggle action
- JavaScript CRUD interface
- Stats dashboard

**5. Notes API with Tags**
- Note and Tag models
- Nested serializers
- Filter by tag

---

## Common Patterns

### API Response Pattern

```python
# Consistent response structure
{
    "status": "success",
    "data": {...},
    "message": "Post created"
}

# Error response
{
    "status": "error",
    "errors": {...},
    "message": "Validation failed"
}
```

### JavaScript Fetch Pattern

```javascript
async function apiCall(url, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    const response = await fetch(url, options);

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    return method === 'DELETE' ? null : await response.json();
}
```

### Loading State Pattern

```javascript
async function loadData() {
    const container = document.getElementById('container');
    container.innerHTML = '<p>Loading...</p>';

    try {
        const data = await fetch('/api/data/').then(r => r.json());
        container.innerHTML = '';
        // Render data
    } catch (error) {
        container.innerHTML = '<p>Error loading data</p>';
    }
}
```

---

## Security Best Practices

**API Security:**
- Use authentication for write operations
- Validate all input with serializers
- Use proper HTTP status codes
- Rate limit API endpoints
- Don't expose sensitive data

**JavaScript Security:**
- Always include CSRF token
- Validate/sanitize user input
- Don't store sensitive data in localStorage
- Use HTTPS in production

---

## Debugging Tips

### API Debugging

1. **Use browsable API** - Test directly in browser
2. **Check Network tab** - See requests/responses
3. **Print serializer.errors** - See validation issues
4. **Use Postman/Insomnia** - Advanced API testing

### JavaScript Debugging

1. **console.log()** - Print values
2. **Browser DevTools** - Network, Console, Elements
3. **debugger;** - Set breakpoints in code
4. **Network tab** - Check API responses

---

## Additional Resources

- **Postman** - API testing tool
- **Insomnia** - Alternative to Postman
- **HTTPie** - Command-line HTTP client
- **JSON Formatter** - Browser extension for JSON
- **ES6 Features** - Modern JavaScript guide
- **You Don't Know JS** - Free JavaScript book series

---

**Remember:** APIs are the backbone of modern web development. Master them!
