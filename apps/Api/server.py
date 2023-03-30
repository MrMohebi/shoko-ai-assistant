from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from ai.llm.chatGPT35 import ChatGPT35
from cusTypes.GeneralTypes import PromptItem
from utils.PromptManager import PromptManager

app = FastAPI()


class Prompt(BaseModel):
    role: str = "user"
    prompt: str


class Reply(BaseModel):
    status: bool
    data: Optional[str] = None
    response: Optional[str] = None


@app.get("/")
async def filter_str():
    return Reply(status=True, data="Hello World")


@app.post("/talk")
async def filter_str(request: Prompt):
    inpPrompt = PromptItem(start=request.role, text=request.prompt, connector_parts=":")
    promptManager = PromptManager(inpPrompt)
    promptManager.addMiddleware(["defaultPrompts"])
    chatGPT35 = ChatGPT35()
    result = chatGPT35.chat(promptManager)
    return Reply(status=True, response=result)
