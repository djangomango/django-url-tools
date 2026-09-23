from typing import Any
from urllib.parse import quote, quote_plus

from django import template

from ..helpers import UrlHelper

register = template.Library()


@register.simple_tag
def add_params(url: Any, **kwargs: Any) -> str:
    """Update query parameters on target URL and return new URL."""
    helper = UrlHelper(url)
    try:
        helper.update_query_data(**kwargs)
        return helper.get_full_path()
    except Exception:
        return ""


@register.simple_tag
def del_params(url: Any, *args: Any, **kwargs: Any) -> str:
    """Remove specified query parameters from target URL and return new URL."""
    helper = UrlHelper(url)
    try:
        helper.del_params(*args, **kwargs)
        return helper.get_full_path()
    except Exception:
        return ""


@register.simple_tag
def overload_params(url: Any, **kwargs: Any) -> str:
    """Append query parameter values to target URL and return new URL."""
    helper = UrlHelper(url)
    try:
        helper.overload_params(**kwargs)
        return helper.get_full_path()
    except Exception:
        return ""


@register.simple_tag
def url_params(url: Any, **kwargs: Any) -> str:
    """Update URL query parameters and return full URL string."""
    helper = UrlHelper(url)
    helper.update_query_data(**kwargs)
    return helper.get_full_path()


@register.simple_tag
def toggle_params(url: Any, **kwargs: Any) -> str:
    """Toggle presence of query parameter key/value on target URL."""
    helper = UrlHelper(url)
    helper.toggle_params(**kwargs)
    return helper.get_full_path()


@register.filter(name="quote")
def quote_param(value: str, safe: str = "/") -> str:
    """URL-encode string using urllib.parse.quote."""
    return quote(value, safe)


@register.filter(name="quote_plus")
def quote_param_plus(value: str, safe: str = "/") -> str:
    """URL-encode string using urllib.parse.quote_plus."""
    return quote_plus(value, safe)
