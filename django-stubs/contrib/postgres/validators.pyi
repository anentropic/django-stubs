from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from django.core.validators import MaxLengthValidator, MaxValueValidator, MinLengthValidator, MinValueValidator

class ArrayMaxLengthValidator(MaxLengthValidator): ...
class ArrayMinLengthValidator(MinLengthValidator): ...

class KeysValidator:
    messages: dict[str, str]
    strict: bool
    def __init__(self, keys: Iterable[str], strict: bool = ..., messages: Mapping[str, str] | None = ...) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def deconstruct(obj) -> tuple[str, Sequence[Any], dict[str, Any]]: ...  # fake

class RangeMaxValueValidator(MaxValueValidator): ...
class RangeMinValueValidator(MinValueValidator): ...
