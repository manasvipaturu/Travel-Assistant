# main.py
import argparse
from app.assistant import TravelAssistant

def main():
    parser = argparse.ArgumentParser(description="Travel Assistant")
    parser.add_argument("--query", type=str, help="Query for the travel assistant")
    args = parser.parse_args()

    assistant = TravelAssistant()
    response = assistant.answer_question(args.query)
    print(response)

if __name__ == "__main__":
    main()
