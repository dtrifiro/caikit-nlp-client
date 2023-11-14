from collections.abc import Iterable

import pytest


@pytest.fixture(scope="session")
def caikit_test_producer():
    from caikit.interfaces.nlp.data_model.text_generation import ProducerId

    yield ProducerId(
        name="Testing Producer",
        version="0.0.1",
    )


@pytest.fixture(scope="session")
def generated_text():
    yield "a symphony"


@pytest.fixture(scope="session")
def generated_text_result(caikit_test_producer, generated_text):
    from caikit.interfaces.nlp.data_model.text_generation import (
        FinishReason,
        GeneratedTextResult,
    )

    yield GeneratedTextResult(
        generated_text=generated_text,
        generated_tokens=42,
        finish_reason=FinishReason.EOS_TOKEN,
        producer_id=caikit_test_producer,
        input_token_count=10,
        seed=None,  # Optional[np.uint64]
    )


# FIXME: Validate text stream mocking. There's a lot of logic here.
#        Can this be simplified?
@pytest.fixture(scope="session")
def generated_text_stream_result(caikit_test_producer, generated_text):
    from caikit.interfaces.nlp.data_model.text_generation import (
        FinishReason,
        GeneratedTextStreamResult,
        GeneratedToken,
        TokenStreamDetails,
    )

    split_text = ["", "life", " is", " ", "a", " state", " of", " being", ""]

    # TODO: validate token_list
    token_list = [GeneratedToken(text="dummy generated token value", logprob=0.42)]
    input_token_count = len(split_text)

    result = []
    for text in split_text:
        details = TokenStreamDetails(
            finish_reason=FinishReason.NOT_FINISHED,
            generated_tokens=42,  # FIXME: is this correct?
            seed=None,
            input_token_count=input_token_count,
        )

        stream_result = GeneratedTextStreamResult(
            generated_text=text,
            tokens=token_list,
            details=details,
        )

        result.append(stream_result)

    result[-1].details.finish_reason = FinishReason.EOS_TOKEN
    return result


@pytest.fixture(scope="session")
def mock_text_generation(
    generated_text_result, generated_text_stream_result, monkeysession
):
    # import caikit_nlp.modules.text_generation.text_generation_local
    import caikit_nlp.modules.text_generation.text_generation_tgis
    from caikit.interfaces.nlp.data_model.text_generation import (
        GeneratedTextResult,
        GeneratedTextStreamResult,
    )

    # NOTE: config uses tgis, so this is not really required,
    #       unless we want to test the local text generation module
    # monkeypatch.setattr(
    #     caikit_nlp.modules.text_generation.text_generation_local,
    #     "generate_text_func",
    #     lambda: generated_text_result,
    # )

    class StubTGISGenerationClient:
        def __init__(self, *args, **kwargs):
            pass

        def unary_generate(self, *args, **kwargs) -> GeneratedTextResult:
            return generated_text_result

        def stream_generate(
            self, *args, **kwargs
        ) -> Iterable[GeneratedTextStreamResult]:
            yield from generated_text_stream_result

    monkeysession.setattr(
        caikit_nlp.modules.text_generation.text_generation_tgis,
        "TGISGenerationClient",
        StubTGISGenerationClient,
    )

    yield
