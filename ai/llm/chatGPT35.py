import pathlib
import openai

from utils import PromptManager
from utils.Base import ReadConfig


class ChatGPT35:
    def __init__(self):
        CONFIG_FILE = str(pathlib.Path.cwd()) + "/configs/ais.toml"
        if not pathlib.Path(CONFIG_FILE).exists():
            raise FileNotFoundError("Cant find configs/ais.toml")

        config = ReadConfig().parseFile(CONFIG_FILE)
        self.ctrlConfig = config.AI.chatGPT35
        self.model = self.ctrlConfig.model
        if self.ctrlConfig is None:
            raise FileNotFoundError("there is no config for ChatGPT3.5 in configs/ais.toml")

        openai.api_key = self.ctrlConfig.apiToken

    def chat(self, promptManager: PromptManager) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=promptManager.openAiFormat(),
                temperature=self.ctrlConfig.temperature or 0.5,
                max_tokens=self.ctrlConfig.maxTokens or 100,
                presence_penalty=self.ctrlConfig.presencePenalty or 0.0,
                frequency_penalty=self.ctrlConfig.frequencyPenalty or 0.0,
                n=1
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(e)
            return "Error"
