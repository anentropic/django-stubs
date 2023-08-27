from typing import Any, Optional, Union
from uuid import UUID

from django.db.models.options import Options
from django.template.context import RequestContext
from django.utils.safestring import SafeText

register: Any

def admin_urlname(value: Options[Any], arg: SafeText) -> str: ...
def admin_urlquote(value: Union[int, str, UUID]) -> Union[int, str, UUID]: ...
def add_preserved_filters(
    context: Union[dict[str, Union[Options[Any], str]], RequestContext],
    url: str,
    popup: bool = ...,
    to_field: Optional[str] = ...,
) -> str: ...
