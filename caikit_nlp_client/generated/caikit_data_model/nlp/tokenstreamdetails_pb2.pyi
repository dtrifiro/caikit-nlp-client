from caikit_nlp_client.generated.caikit_data_model.nlp import finishreason_pb2 as _finishreason_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenStreamDetails(_message.Message):
    __slots__ = ["finish_reason", "generated_tokens", "seed", "input_token_count"]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    GENERATED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    finish_reason: _finishreason_pb2.FinishReason
    generated_tokens: int
    seed: int
    input_token_count: int
    def __init__(self, finish_reason: _Optional[_Union[_finishreason_pb2.FinishReason, str]] = ..., generated_tokens: _Optional[int] = ..., seed: _Optional[int] = ..., input_token_count: _Optional[int] = ...) -> None: ...
