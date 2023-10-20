from caikit_nlp_client.generated.caikit_data_model.caikit_nlp import exponentialdecaylengthpenalty_pb2 as _exponentialdecaylengthpenalty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextGenerationTaskRequest(_message.Message):
    __slots__ = ["text", "max_new_tokens", "min_new_tokens", "truncate_input_tokens", "decoding_method", "top_k", "top_p", "typical_p", "temperature", "seed", "repetition_penalty", "max_time", "exponential_decay_length_penalty", "stop_sequences", "preserve_input_text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MAX_NEW_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MIN_NEW_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    DECODING_METHOD_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    TYPICAL_P_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    REPETITION_PENALTY_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPONENTIAL_DECAY_LENGTH_PENALTY_FIELD_NUMBER: _ClassVar[int]
    STOP_SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_INPUT_TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    max_new_tokens: int
    min_new_tokens: int
    truncate_input_tokens: int
    decoding_method: str
    top_k: int
    top_p: float
    typical_p: float
    temperature: float
    seed: int
    repetition_penalty: float
    max_time: float
    exponential_decay_length_penalty: _exponentialdecaylengthpenalty_pb2.ExponentialDecayLengthPenalty
    stop_sequences: _containers.RepeatedScalarFieldContainer[str]
    preserve_input_text: bool
    def __init__(self, text: _Optional[str] = ..., max_new_tokens: _Optional[int] = ..., min_new_tokens: _Optional[int] = ..., truncate_input_tokens: _Optional[int] = ..., decoding_method: _Optional[str] = ..., top_k: _Optional[int] = ..., top_p: _Optional[float] = ..., typical_p: _Optional[float] = ..., temperature: _Optional[float] = ..., seed: _Optional[int] = ..., repetition_penalty: _Optional[float] = ..., max_time: _Optional[float] = ..., exponential_decay_length_penalty: _Optional[_Union[_exponentialdecaylengthpenalty_pb2.ExponentialDecayLengthPenalty, _Mapping]] = ..., stop_sequences: _Optional[_Iterable[str]] = ..., preserve_input_text: bool = ...) -> None: ...
