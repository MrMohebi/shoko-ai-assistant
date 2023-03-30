import importlib
import pathlib

from loguru import logger

from cusTypes.GeneralTypes import PromptItem


class PromptManager:
    def __init__(self, prompt: PromptItem, additionalPrompts=None):
        if additionalPrompts is None:
            additionalPrompts = []

        self.additionalPrompts = additionalPrompts
        self.initPrompt = prompt
        self.promptHistory = []

    def addAdditionalPrompt(self, prompt: PromptItem):
        self.additionalPrompts.append(prompt)

    def addAdditionalPromptsArray(self, prompts: [PromptItem]):
        self.additionalPrompts += prompts

    def getPrompt(self) -> [PromptItem]:
        return self.additionalPrompts + [self.initPrompt]

    def toArray(self) -> list:
        result = []
        for i in self.getPrompt():
            result.append(i.toDict())
        return result

    def addMiddleware(self, middlewares: [str]):
        for middleware in middlewares:
            if not pathlib.Path(f"middleware/{middleware}/main.py").exists():
                logger.warning(f"Skip Middleware {middleware} ,Do Not Exist.")
                continue
            module = importlib.import_module('middleware.' + middleware + ".main")
            resultPrompts = module.Main(self.initPrompt).run()
            if resultPrompts is None:
                resultPrompts = []
            self.addAdditionalPromptsArray(resultPrompts)
