from collections.abc import Iterator, Mapping
from typing import Any, Optional, Union

from django.forms.utils import ErrorDict

class FieldDoesNotExist(Exception): ...
class AppRegistryNotReady(Exception): ...

class ObjectDoesNotExist(Exception):
    silent_variable_failure: bool = ...

class MultipleObjectsReturned(Exception): ...
class SuspiciousOperation(Exception): ...
class SuspiciousMultipartForm(SuspiciousOperation): ...
class SuspiciousFileOperation(SuspiciousOperation): ...
class DisallowedHost(SuspiciousOperation): ...
class DisallowedRedirect(SuspiciousOperation): ...
class TooManyFieldsSent(SuspiciousOperation): ...
class RequestDataTooBig(SuspiciousOperation): ...
class RequestAborted(Exception): ...
class BadRequest(Exception): ...
class PermissionDenied(Exception): ...
class ViewDoesNotExist(Exception): ...
class MiddlewareNotUsed(Exception): ...
class ImproperlyConfigured(Exception): ...
class FieldError(Exception): ...

NON_FIELD_ERRORS: str

class ValidationError(Exception):
    error_dict: Any = ...
    error_list: Any = ...
    message: Any = ...
    code: Any = ...
    params: Any = ...
    def __init__(
        self,
        message: Any,
        code: Optional[str] = ...,
        params: Optional[Mapping[str, Any]] = ...,
    ) -> None: ...
    @property
    def message_dict(self) -> dict[str, list[str]]: ...
    @property
    def messages(self) -> list[str]: ...
    def update_error_dict(
        self, error_dict: Mapping[str, Any]
    ) -> Union[dict[str, list[ValidationError]], ErrorDict]: ...
    def __iter__(self) -> Iterator[Union[tuple[str, list[str]], str]]: ...

class EmptyResultSet(Exception): ...
class SynchronousOnlyOperation(Exception): ...
