from collections.abc import Iterator, Mapping, Sequence
from typing import Any, Generic, TypeVar

class ConnectionProxy:
    def __init__(self, connections: Mapping[str, Any], alias: str) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class ConnectionDoesNotExist(Exception): ...

_T = TypeVar("_T")

class BaseConnectionHandler(Generic[_T]):
    settings_name: str | None
    exception_class: type[Exception]
    thread_critical: bool
    def __init__(self, settings: Any | None = ...) -> None: ...
    @property
    def settings(self) -> dict[str, Any]: ...
    def configure_settings(self, settings: dict[str, Any] | None) -> dict[str, Any]: ...
    def create_connection(self, alias: str) -> _T: ...
    def __getitem__(self, alias: str) -> _T: ...
    def __setitem__(self, key: str, value: _T) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def all(self) -> Sequence[_T]: ...