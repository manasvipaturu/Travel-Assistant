# Import necessary libraries
import argparse
from app.assistant import TravelAssistant

# Define the main function for the Travel Assistant
def main():
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Travel Assistant")

    # Add a command-line argument to accept the user's query
    parser.add_argument("--query", type=str, help="Query for the travel assistant")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Create an instance of the TravelAssistant class
    assistant = TravelAssistant()

    # Use the assistant to answer the user's query
    response = assistant.answer_question(args.query)

    # Print the response to the console
    print(response)

# Check if this script is the main entry point
if __name__ == "__main__":
    # If it is, call the main function
    main()

