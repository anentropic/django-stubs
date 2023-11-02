from collections.abc import Sequence
from typing import Any

from django.utils._os import _PathCompatible
from django.utils.functional import cached_property

from .base import Storage
from .mixins import StorageSettingsMixin

class InMemoryStorage(Storage, StorageSettingsMixin):
    def __init__(
        self,
        location: _PathCompatible | None = ...,
        base_url: str | None = ...,
        file_permissions_mode: int | None = ...,
        directory_permissions_mode: int | None = ...,
    ) -> None: ...
    @cached_property
    def base_location(self) -> _PathCompatible: ...
    @cached_property
    def location(self) -> _PathCompatible: ...
    @cached_property
    def base_url(self) -> str: ...
    @cached_property
    def file_permissions_mode(self) -> int | None: ...
    @cached_property
    def directory_permissions_mode(self) -> int | None: ...
    def deconstruct(obj) -> tuple[str, Sequence[Any], dict[str, Any]]: ...  # fake