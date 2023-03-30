from cusTypes.GeneralTypes import PromptItem


def MorningCharacter() -> [PromptItem]:
    return [
        PromptItem(start="system", text="You are a weather forecast reporter", connector_parts=":"),
        PromptItem(start="user", text="tell me today weather forecast", connector_parts=":"),
    ]
