from middleware.defaultPrompts.prompts import MorningCharacter
from cusTypes.GeneralTypes import PromptItem
import re

class Main:
    def __init__(self, userPrompt: PromptItem):
        self.userPrompt = userPrompt

    def run(self) -> [PromptItem]:
        return self.defaultPrompts(self.userPrompt)

    @staticmethod
    def defaultPrompts(userPrompt: PromptItem) -> [PromptItem]:
        print(userPrompt.text)

        # morning character
        keywords = ['morning']
        if any(ext in userPrompt.text for ext in keywords):
            return MorningCharacter() or []
