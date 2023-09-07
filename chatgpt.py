import openai


class ChatGPT:
    """
    """
    api_key = ""

    def init(self,api_key):
        openai.api_key = api_key

    def ask(self,prompt, role=None, max_tokens=None):
        message = [{"role": "user", "content": prompt}]
        if role:
            message.append(
                {
                    "role": "system",
                    "content": role,
                }
            )
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message,
            max_tokens=max_tokens,
        )

        return completion["choices"][0]["message"]["content"].strip()