import getpass

import openai

from . import color, settings


class ChatGPT:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        self.model = settings.GPT_MODEL
        self.timeout = settings.REQUEST_TIMEOUT
        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            }
        ]

    def print_greeting(self):
        print(color.Color.GREEN + f"Hello, {getpass.getuser()}🤖" + color.Color.END)
        print(color.Color.PURPLE + f"Current model: {self.model},\nTimeout: {self.timeout}" + color.Color.END)

    def send(self, prompt: str) -> dict[str, str]:
        self.messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            timeout=self.timeout,
        )

        reply = response.choices[0].message.content.strip()
        consumed_token = response.usage.total_tokens
        answer = {"reply": reply, "consumed_tokens": consumed_token}

        self.messages.append({"role": "assistant", "content": reply})

        return answer
