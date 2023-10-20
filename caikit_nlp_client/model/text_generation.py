from enum import Enum
from dataclasses import dataclass


class FinishReason(Enum):
    NOT_FINISHED: 1
    MAX_TOKENS: 2
    EOS_TOKEN: 3
    CANCELLED: 4
    TIME_LIMIT: 5
    STOP_SEQUENCE: 6
    TOKEN_LIMIT: 7
    ERROR: 8


@dataclass
class ProducerId:
    name: str
    version: str


@dataclass
class TextGenerationTaskResult:
    generated_text: str
    """
    generated_tokens: int
    finish_reason: FinishReason
    producer_id: ProducerId
    input_token_count: int
    seed: int
    """

@dataclass
class ExponentialDecayLengthPenalty:
    start_index: int
    decay_factor: float

@dataclass
class TextGenerationTask:
    model_id: str
    text: str
    """  
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
    exponential_decay_length_penalty: ExponentialDecayLengthPenalty
    stop_sequences: [str]
    preserve_input_text: bool
    """