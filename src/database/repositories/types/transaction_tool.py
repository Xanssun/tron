from typing import Required, TypedDict


class SavePrivateKeyType(TypedDict):
    verification_code_id: Required[int]
    private_key: Required[bytes]
    verification_code: Required[str]
