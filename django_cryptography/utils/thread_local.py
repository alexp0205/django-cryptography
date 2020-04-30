from threading import local
from typing import Optional

from django_cryptography.utils.crypto import FernetBytes

_thread_locals = local()

CRYPTER_KEY_ATTR_NAME = "_CRYPTER_KEY_ATTR_NAME"


def set_encryption_key(encryption_key: Optional[bytes]):
    if encryption_key:
        crypter = FernetBytes(key=encryption_key)
    else:
        crypter = None
    setattr(_thread_locals, CRYPTER_KEY_ATTR_NAME, crypter)


def get_crypter() -> Optional[FernetBytes]:
    return getattr(_thread_locals, CRYPTER_KEY_ATTR_NAME, None)
