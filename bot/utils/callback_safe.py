
import hashlib
from typing import Iterable, Optional

def encode(prefix: str, value: str) -> str:
    """Return callback data as prefix + sha1(value). Ensures <=64 bytes if prefix <=24."""
    h = hashlib.sha1(value.encode("utf-8")).hexdigest()
    return f"{prefix}{h}"

def decode(prefix: str, data: str, candidates: Iterable[str]) -> Optional[str]:
    """Find original value among candidates by matching sha1.
    Returns the matched value or None.
    """
    if not data.startswith(prefix):
        return None
    token = data[len(prefix):]
    for v in candidates:
        if hashlib.sha1(v.encode("utf-8")).hexdigest() == token:
            return v
    return None
