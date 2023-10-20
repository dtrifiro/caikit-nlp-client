from caikit_nlp_client.generated.caikit_data_model.nlp import token_pb2 as _token_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenizationResults(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_token_pb2.Token]
    def __init__(self, results: _Optional[_Iterable[_Union[_token_pb2.Token, _Mapping]]] = ...) -> None: ...
