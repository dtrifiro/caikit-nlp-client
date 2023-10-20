from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TuningConfig(_message.Message):
    __slots__ = ["num_virtual_tokens", "prompt_tuning_init_text", "prompt_tuning_init_method", "prompt_tuning_init_source_model", "output_model_types"]
    NUM_VIRTUAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TUNING_INIT_TEXT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TUNING_INIT_METHOD_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TUNING_INIT_SOURCE_MODEL_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MODEL_TYPES_FIELD_NUMBER: _ClassVar[int]
    num_virtual_tokens: int
    prompt_tuning_init_text: str
    prompt_tuning_init_method: str
    prompt_tuning_init_source_model: str
    output_model_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, num_virtual_tokens: _Optional[int] = ..., prompt_tuning_init_text: _Optional[str] = ..., prompt_tuning_init_method: _Optional[str] = ..., prompt_tuning_init_source_model: _Optional[str] = ..., output_model_types: _Optional[_Iterable[str]] = ...) -> None: ...
