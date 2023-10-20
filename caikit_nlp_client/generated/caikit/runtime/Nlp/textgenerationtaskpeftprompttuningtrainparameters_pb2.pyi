from caikit_nlp_client.generated.caikit.runtime.Nlp import datastreamsourcegenerationtrainrecord_pb2 as _datastreamsourcegenerationtrainrecord_pb2
from caikit_nlp_client.generated.caikit_data_model.caikit_nlp import tuningconfig_pb2 as _tuningconfig_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextGenerationTaskPeftPromptTuningTrainParameters(_message.Message):
    __slots__ = ["base_model", "train_stream", "tuning_config", "val_stream", "device", "tuning_type", "num_epochs", "learning_rate", "verbalizer", "batch_size", "max_source_length", "max_target_length", "accumulate_steps", "torch_dtype", "silence_progress_bars", "seed"]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    TRAIN_STREAM_FIELD_NUMBER: _ClassVar[int]
    TUNING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VAL_STREAM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    TUNING_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    VERBALIZER_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_SOURCE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_TARGET_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATE_STEPS_FIELD_NUMBER: _ClassVar[int]
    TORCH_DTYPE_FIELD_NUMBER: _ClassVar[int]
    SILENCE_PROGRESS_BARS_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    base_model: str
    train_stream: _datastreamsourcegenerationtrainrecord_pb2.DataStreamSourceGenerationTrainRecord
    tuning_config: _tuningconfig_pb2.TuningConfig
    val_stream: _datastreamsourcegenerationtrainrecord_pb2.DataStreamSourceGenerationTrainRecord
    device: str
    tuning_type: str
    num_epochs: int
    learning_rate: float
    verbalizer: str
    batch_size: int
    max_source_length: int
    max_target_length: int
    accumulate_steps: int
    torch_dtype: str
    silence_progress_bars: bool
    seed: int
    def __init__(self, base_model: _Optional[str] = ..., train_stream: _Optional[_Union[_datastreamsourcegenerationtrainrecord_pb2.DataStreamSourceGenerationTrainRecord, _Mapping]] = ..., tuning_config: _Optional[_Union[_tuningconfig_pb2.TuningConfig, _Mapping]] = ..., val_stream: _Optional[_Union[_datastreamsourcegenerationtrainrecord_pb2.DataStreamSourceGenerationTrainRecord, _Mapping]] = ..., device: _Optional[str] = ..., tuning_type: _Optional[str] = ..., num_epochs: _Optional[int] = ..., learning_rate: _Optional[float] = ..., verbalizer: _Optional[str] = ..., batch_size: _Optional[int] = ..., max_source_length: _Optional[int] = ..., max_target_length: _Optional[int] = ..., accumulate_steps: _Optional[int] = ..., torch_dtype: _Optional[str] = ..., silence_progress_bars: bool = ..., seed: _Optional[int] = ...) -> None: ...
