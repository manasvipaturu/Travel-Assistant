# assistant.py
import openai

class TravelAssistant:
    def __init__(self):
        openai.api_key = 'API_KEY'

    def answer_question(self, question):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            max_tokens=100
        )
        return response.choices[0].text

