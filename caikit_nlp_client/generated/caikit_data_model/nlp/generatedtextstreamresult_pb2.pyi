from caikit_nlp_client.generated.caikit_data_model.common import producerid_pb2 as _producerid_pb2
from caikit_nlp_client.generated.caikit_data_model.nlp import generatedtoken_pb2 as _generatedtoken_pb2
from caikit_nlp_client.generated.caikit_data_model.nlp import tokenstreamdetails_pb2 as _tokenstreamdetails_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeneratedTextStreamResult(_message.Message):
    __slots__ = ["generated_text", "tokens", "details", "producer_id"]
    GENERATED_TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_ID_FIELD_NUMBER: _ClassVar[int]
    generated_text: str
    tokens: _containers.RepeatedCompositeFieldContainer[_generatedtoken_pb2.GeneratedToken]
    details: _tokenstreamdetails_pb2.TokenStreamDetails
    producer_id: _producerid_pb2.ProducerId
    def __init__(self, generated_text: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[_generatedtoken_pb2.GeneratedToken, _Mapping]]] = ..., details: _Optional[_Union[_tokenstreamdetails_pb2.TokenStreamDetails, _Mapping]] = ..., producer_id: _Optional[_Union[_producerid_pb2.ProducerId, _Mapping]] = ...) -> None: ...
