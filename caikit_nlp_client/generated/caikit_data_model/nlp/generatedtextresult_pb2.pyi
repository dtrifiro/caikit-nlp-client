from caikit_nlp_client.generated.caikit_data_model.common import producerid_pb2 as _producerid_pb2
from caikit_nlp_client.generated.caikit_data_model.nlp import finishreason_pb2 as _finishreason_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeneratedTextResult(_message.Message):
    __slots__ = ["generated_text", "generated_tokens", "finish_reason", "producer_id", "input_token_count", "seed"]
    GENERATED_TEXT_FIELD_NUMBER: _ClassVar[int]
    GENERATED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    generated_text: str
    generated_tokens: int
    finish_reason: _finishreason_pb2.FinishReason
    producer_id: _producerid_pb2.ProducerId
    input_token_count: int
    seed: int
    def __init__(self, generated_text: _Optional[str] = ..., generated_tokens: _Optional[int] = ..., finish_reason: _Optional[_Union[_finishreason_pb2.FinishReason, str]] = ..., producer_id: _Optional[_Union[_producerid_pb2.ProducerId, _Mapping]] = ..., input_token_count: _Optional[int] = ..., seed: _Optional[int] = ...) -> None: ...
