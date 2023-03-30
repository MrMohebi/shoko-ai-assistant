from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from cusTypes.GeneralTypes import PromptItem
from utils.PromptManager import PromptManager

app = FastAPI()


class Prompt(BaseModel):
    role: str = "user"
    prompt: str


class Reply(BaseModel):
    status: bool
    data: Optional[bytes] = None
    response: Optional[dict] = None


@app.get("/")
async def filter_str():
    return Reply(status=True, data=b"Hello World")


@app.post("/talk")
async def filter_str(request: Prompt):
    inpPrompt = PromptItem(start=request.role, text=request.prompt, connector_parts=":")
    promptManager = PromptManager(inpPrompt)
    promptManager.addMiddleware(["defaultPrompts"])
    print(promptManager.toArray())
    return Reply(status=True, data=b"aaaaa")
