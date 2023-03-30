import shortuuid as shortuuid
from pydantic import BaseModel, validator, root_validator
from typing import Optional, List
import time


class PromptItem(BaseModel):
    id: str = str(shortuuid.uuid())
    start: str = ""
    text: str
    connector_parts: str = ":"

    @property
    def prompt(self):
        return f"{self.start}{self.connector_parts}{self.text}"

    @root_validator
    def start_check(cls, values):
        start, connect_words = values.get('start'), values.get('connector_parts')
        if len(start) > 50:
            raise ValueError('start name too long')
        if not start:
            values["start"] = "*"
        if connect_words:
            values["start"] = start.strip().rstrip(connect_words)
        return values

    @validator('text')
    def text_check(cls, v):
        if not v:
            return "None"
        return v

    def toDict(self):
        return dict(self)


class LlmReturn(BaseModel):
    model_flag: Optional[str]
    prompt: str
    reply: List[str]
    usage: Optional[int]
    time: int = int(time.time())
    raw: Optional[dict]