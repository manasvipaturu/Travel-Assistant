#assistant
import openai
import json

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

    def recommend_city(self, city):
        with open('data/city_data.json', 'r') as file:
            city_data = json.load(file)
            if city in city_data:
                hotels = city_data[city]['hotels']
                restaurants = city_data[city]['restaurants']
                activities = city_data[city]['activities']

                with open('templates/responses/recommendations.txt', 'r') as template_file:
                    template = template_file.read()
                    response = template.format(city=city, hotels=', '.join(hotels), restaurants=', '.join(restaurants), activities=', '.join(activities))

        return response


