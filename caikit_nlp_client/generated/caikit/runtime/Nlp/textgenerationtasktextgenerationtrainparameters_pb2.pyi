from caikit_nlp_client.generated.caikit.runtime.Nlp import datastreamsourcegenerationtrainrecord_pb2 as _datastreamsourcegenerationtrainrecord_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextGenerationTaskTextGenerationTrainParameters(_message.Message):
    __slots__ = ["base_model", "train_stream", "torch_dtype", "max_source_length", "max_target_length", "batch_size", "num_epochs", "accumulate_steps", "random_seed", "lr", "use_iterable_dataset"]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    TRAIN_STREAM_FIELD_NUMBER: _ClassVar[int]
    TORCH_DTYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_SOURCE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_TARGET_LENGTH_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATE_STEPS_FIELD_NUMBER: _ClassVar[int]
    RANDOM_SEED_FIELD_NUMBER: _ClassVar[int]
    LR_FIELD_NUMBER: _ClassVar[int]
    USE_ITERABLE_DATASET_FIELD_NUMBER: _ClassVar[int]
    base_model: str
    train_stream: _datastreamsourcegenerationtrainrecord_pb2.DataStreamSourceGenerationTrainRecord
    torch_dtype: str
    max_source_length: int
    max_target_length: int
    batch_size: int
    num_epochs: int
    accumulate_steps: int
    random_seed: int
    lr: float
    use_iterable_dataset: bool
    def __init__(self, base_model: _Optional[str] = ..., train_stream: _Optional[_Union[_datastreamsourcegenerationtrainrecord_pb2.DataStreamSourceGenerationTrainRecord, _Mapping]] = ..., torch_dtype: _Optional[str] = ..., max_source_length: _Optional[int] = ..., max_target_length: _Optional[int] = ..., batch_size: _Optional[int] = ..., num_epochs: _Optional[int] = ..., accumulate_steps: _Optional[int] = ..., random_seed: _Optional[int] = ..., lr: _Optional[float] = ..., use_iterable_dataset: bool = ...) -> None: ...
