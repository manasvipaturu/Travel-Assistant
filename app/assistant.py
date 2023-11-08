# Import necessary libraries
import openai
import json

# Define a Travel Assistant class
class TravelAssistant:
    def __init__(self):
        # Set the OpenAI API key
        openai.api_key = 'API_KEY'  # Replace 'API_KEY' with your actual API key

    # Answer a travel-related question
    def answer_question(self, question):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            max_tokens=100
        )
        return response.choices[0].text

    # Provide recommendations for a specific city
    def recommend_city(self, city):
        # Load city data from a JSON file (from available options as of now)
        with open('data/city_data.json', 'r') as file:
            city_data = json.load(file)

            # Check if the city is in the data
            if city in city_data:
                hotels = city_data[city]['hotels']
                restaurants = city_data[city]['restaurants']
                activities = city_data[city]['activities']

                # Load a response template
                with open('templates/responses/recommendations.txt', 'r') as template_file:
                    template = template_file.read()

                # Populate the response template with data
                response = template.format(city=city, hotels=', '.join(hotels), restaurants=', '.join(restaurants), activities=', '.join(activities))
        #add error handling and a user-friendly response for cases where the requested city is not found in the data.
        return response



