from caikit_nlp_client.generated.caikit_data_model.nlp import finishreason_pb2 as _finishreason_pb2
from caikit_nlp_client.generated.caikit_data_model.nlp import tokenclassificationresult_pb2 as _tokenclassificationresult_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClassifiedGeneratedTextStreamResult(_message.Message):
    __slots__ = ["text", "token_classification_results", "finish_reason", "token_count", "seed", "processed_index"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CLASSIFICATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_INDEX_FIELD_NUMBER: _ClassVar[int]
    text: str
    token_classification_results: _containers.RepeatedCompositeFieldContainer[_tokenclassificationresult_pb2.TokenClassificationResult]
    finish_reason: _finishreason_pb2.FinishReason
    token_count: int
    seed: int
    processed_index: int
    def __init__(self, text: _Optional[str] = ..., token_classification_results: _Optional[_Iterable[_Union[_tokenclassificationresult_pb2.TokenClassificationResult, _Mapping]]] = ..., finish_reason: _Optional[_Union[_finishreason_pb2.FinishReason, str]] = ..., token_count: _Optional[int] = ..., seed: _Optional[int] = ..., processed_index: _Optional[int] = ...) -> None: ...
