from collections.abc import Callable
from typing import Any, Optional, Union

NONE_ID: Any
NO_RECEIVERS: Any

class Signal:
    receivers: Any = ...
    providing_args: Any = ...
    lock: Any = ...
    use_caching: Any = ...
    sender_receivers_cache: Any = ...
    def __init__(
        self, providing_args: list[str] = ..., use_caching: bool = ...
    ) -> None: ...
    def connect(
        self,
        receiver: Callable[..., Any],
        sender: Optional[object] = ...,
        weak: bool = ...,
        dispatch_uid: Optional[str] = ...,
    ) -> None: ...
    def disconnect(
        self,
        receiver: Optional[Callable[..., Any]] = ...,
        sender: Optional[object] = ...,
        dispatch_uid: Optional[str] = ...,
    ) -> bool: ...
    def has_listeners(self, sender: Any = ...) -> bool: ...
    def send(
        self, sender: Any, **named: Any
    ) -> list[tuple[Callable[..., Any], Optional[str]]]: ...
    def send_robust(
        self, sender: Any, **named: Any
    ) -> list[tuple[Callable[..., Any], Union[ValueError, str]]]: ...

def receiver(
    signal: Union[list[Signal], Signal], **kwargs: Any
) -> Callable[..., Any]: ...
