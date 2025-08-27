import hashlib, time
from typing import Dict, Any

SALT = b"zoran_rgpd_salt_v1"

def pseudonymize(value: str) -> str:
    h = hashlib.sha256(SALT + value.encode()).hexdigest()
    return f"tok_{h[:16]}"

def mask(value: str, keep: int = 3) -> str:
    if not value:
        return value
    return value[:keep] + "*" * max(0, len(value) - keep)

def enforce_ttl(fragment: Dict[str, Any], ttl_seconds: int) -> bool:
    created = fragment.get("created_at", int(time.time()))
    return int(time.time()) - int(created) > ttl_seconds