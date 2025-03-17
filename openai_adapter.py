from openai import OpenAI

class LLMAdapter:
    def __init__(self, settings):
        self.client = OpenAI(api_key=settings['api_key'])
        self.model = settings['model']

    def generate_text(self, system_message, user_message, temperature=0, max_tokens=500):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content