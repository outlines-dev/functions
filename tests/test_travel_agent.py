from outlines.prompts import Prompt
from pydantic import BaseModel

from src.summarization import fn as summarization


def test_summarization():
    assert isinstance(summarization.model_name, str)
    assert isinstance(summarization.schema, type(BaseModel))
    assert isinstance(summarization.prompt_template, Prompt)
