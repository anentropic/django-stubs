from collections.abc import Callable
from typing import Any, Optional, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

def conditional_page(func: _F) -> _F: ...
def require_http_methods(request_method_list: list[str]) -> Callable[[_F], _F]: ...
def require_GET(func: _F) -> _F: ...
def require_POST(func: _F) -> _F: ...
def require_safe(func: _F) -> _F: ...
def condition(
    etag_func: Optional[Callable[..., Any]] = ...,
    last_modified_func: Optional[Callable[..., Any]] = ...,
) -> Callable[[_F], _F]: ...
def etag(etag_func: Callable[..., Any]) -> Callable[[_F], _F]: ...
def last_modified(last_modified_func: Callable[..., Any]) -> Callable[[_F], _F]: ...
