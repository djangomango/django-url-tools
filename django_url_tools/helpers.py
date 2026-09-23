import contextlib
import urllib.parse
from typing import Any

from django.http.request import QueryDict
from django.utils.encoding import iri_to_uri


def del_dict_item_if_exists(dic: dict[Any, Any] | QueryDict, key: Any) -> None:
    """Delete a key from dictionary or QueryDict if present."""
    with contextlib.suppress(KeyError):
        del dic[key]


class UrlHelper:
    """Helper class for parsing, mutating, and serializing request URLs and query parameters."""

    def __init__(self, full_path: Any) -> None:
        """Initialize UrlHelper by parsing a URL path or existing UrlHelper instance."""
        if isinstance(full_path, UrlHelper):
            full_path = full_path.get_full_path()

        r = urllib.parse.urlparse(full_path)

        self.path = r.path
        self.fragment = r.fragment
        self.query_dict = QueryDict(r.query, mutable=True)

    def get_query_string(self, **kwargs: Any) -> str:
        """Return the urlencoded query string."""
        return self.query_dict.urlencode(**kwargs)

    def update_query_data(self, **kwargs: Any) -> None:
        """Update existing query parameters with given keyword arguments."""
        for key, val in kwargs.items():
            if hasattr(val, "__iter__") and not isinstance(val, (str, bytes)):
                self.query_dict.setlist(key, list(val))
            else:
                self.query_dict[key] = val

    def get_full_path(self, **kwargs: Any) -> str:
        """Return full URI path including query parameters and fragment."""
        query_string = self.get_query_string(**kwargs)
        if query_string:
            query_string = f"?{query_string}"

        fragment = (self.fragment and f"#{iri_to_uri(self.fragment)}") or ""

        return f"{iri_to_uri(self.path)}{query_string}{fragment}"

    def overload_params(self, **kwargs: Any) -> None:
        """Append values to existing multi-value query parameter keys."""
        for key, val in kwargs.items():
            uniques = set(self.query_dict.getlist(key))
            uniques.add(val)
            self.query_dict.setlist(key, list(uniques))

    def del_params(self, *params: Any, **kwargs: Any) -> None:
        """Delete specific parameters or parameter prefix values."""
        if not params and not kwargs:
            self.query_dict.clear()
            return

        if params:
            for param in params:
                del_dict_item_if_exists(self.query_dict, param)

        if kwargs:
            for key, val in kwargs.items():
                to_keep = [
                    x for x in self.query_dict.getlist(key) if not x.startswith(val)
                ]
                self.query_dict.setlist(key, to_keep)

    def toggle_params(self, **params: Any) -> None:
        """Toggle presence of query parameter values."""
        for param, value in params.items():
            value = value.decode("utf-8") if hasattr(value, "decode") else str(value)
            if value in self.query_dict.getlist(param):
                self.del_params(**{param: value})
            else:
                self.overload_params(**{param: value})

    def __str__(self) -> str:
        """Return full path representation of UrlHelper."""
        return self.get_full_path()
