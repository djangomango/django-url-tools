# Django-Url-Tools

A Django package providing a comprehensive set of template tags and Python helper utilities to manipulate URL query parameters cleanly and dynamically.

---

## Installation

```bash
pip install git+https://github.com/djangomango/django-url-tools.git@0.1.0
```

Or add to your `requirements.txt`:

```txt
git+https://github.com/djangomango/django-url-tools.git@0.1.0
```

Add `django_url_tools` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "django_url_tools",
    ...
]
```

---

## Usage

### 1. In Django Templates

Load `url_tools` in your templates to update, append, toggle, or remove query parameters:

```html
{% load url_tools %}

<!-- Update or add query parameters to current URL -->
<a href="{% url_params request.get_full_path page=2 sort='name' %}">Next Page</a>

<!-- Append query parameter values -->
<a href="{% overload_params request.get_full_path filter='archived' %}">Add Filter</a>

<!-- Remove specific query parameters -->
<a href="{% del_params request.get_full_path 'filter' %}">Clear Filter</a>

<!-- Toggle query parameter flag -->
<a href="{% toggle_params request.get_full_path active='1' %}">Toggle Active</a>
```

### 2. In Python Code

Manipulate URL query parameters programmatically:

```python
from django_url_tools.helpers import UrlHelper

url = UrlHelper("/search/?category=books&page=1")
url.update_query_data(page=2, order="desc")
print(url.get_full_path())
# Output: /search/?category=books&page=2&order=desc
```

---

## License & Credits

- Licensed under the **BSD License**.
- Originally created by [Monwara LLC](https://bitbucket.org/monwara/django-url-tools/src/master/).