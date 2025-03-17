import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class LLMAdapter:
    def __init__(self, settings):
        self.base_url = settings['base_url']
        self.model = settings['model']

    def generate_text(self, system_message, user_message, temperature=0, max_tokens=500):
        try:
            payload = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "max_tokens": max_tokens
                }
            }
            logging.info(f"Directly calling endpoint {self.base_url} with payload: {payload}")
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["message"]["content"].strip()
        except Exception as e:
            logging.error("Error in chat function: %s", str(e))
            logging.error("Detailed traceback: %s", traceback.format_exc())
            raise
