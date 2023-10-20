from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class S3Base(_message.Message):
    __slots__ = ["endpoint", "region", "bucket", "accessKey", "secretKey", "IAM_id", "IAM_api_key"]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ACCESSKEY_FIELD_NUMBER: _ClassVar[int]
    SECRETKEY_FIELD_NUMBER: _ClassVar[int]
    IAM_ID_FIELD_NUMBER: _ClassVar[int]
    IAM_API_KEY_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    region: str
    bucket: str
    accessKey: str
    secretKey: str
    IAM_id: str
    IAM_api_key: str
    def __init__(self, endpoint: _Optional[str] = ..., region: _Optional[str] = ..., bucket: _Optional[str] = ..., accessKey: _Optional[str] = ..., secretKey: _Optional[str] = ..., IAM_id: _Optional[str] = ..., IAM_api_key: _Optional[str] = ...) -> None: ...
