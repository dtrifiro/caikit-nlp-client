from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TokenClassificationResult(_message.Message):
    __slots__ = ["start", "end", "word", "entity", "entity_group", "score", "token_count"]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    WORD_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    word: str
    entity: str
    entity_group: str
    score: float
    token_count: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., word: _Optional[str] = ..., entity: _Optional[str] = ..., entity_group: _Optional[str] = ..., score: _Optional[float] = ..., token_count: _Optional[int] = ...) -> None: ...
