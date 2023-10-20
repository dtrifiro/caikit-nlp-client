from caikit_nlp_client.generated.caikit.runtime.Nlp import textgenerationtaskpeftprompttuningtrainparameters_pb2 as _textgenerationtaskpeftprompttuningtrainparameters_pb2
from caikit_nlp_client.generated.caikit_data_model.common import s3path_pb2 as _s3path_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextGenerationTaskPeftPromptTuningTrainRequest(_message.Message):
    __slots__ = ["model_name", "output_path", "parameters"]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    output_path: _s3path_pb2.S3Path
    parameters: _textgenerationtaskpeftprompttuningtrainparameters_pb2.TextGenerationTaskPeftPromptTuningTrainParameters
    def __init__(self, model_name: _Optional[str] = ..., output_path: _Optional[_Union[_s3path_pb2.S3Path, _Mapping]] = ..., parameters: _Optional[_Union[_textgenerationtaskpeftprompttuningtrainparameters_pb2.TextGenerationTaskPeftPromptTuningTrainParameters, _Mapping]] = ...) -> None: ...
