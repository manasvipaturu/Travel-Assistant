# Travel Assistant with GPT

This is a simple travel assistant project that uses the OpenAI GPT-3 model to answer travel-related questions. It's a starting point for building a more complex travel assistant.

## Getting Started

### Prerequisites

- Python 3.x
- An OpenAI GPT-3 API key

### Installation

1. Clone this repository to your local machine:

git clone https://github.com/your-username/travel-assistant.git
cd travel-assistant

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate # On Windows, use 'venv\Scripts\activate'


3. Install the required packages:

pip install -r requirements.txt
 
4. Replace `'YOUR_API_KEY'` in `assistant.py` with your actual OpenAI API key.

### Usage

To interact with the travel assistant, run the `main.py` script with a question as a command-line argument. For example:

python main.py --query "What's the weather like in Paris?"


The assistant will generate a response based on your question using the GPT-3 model.

### Customize

You can expand and customize the functionality of the travel assistant by modifying the `assistant.py` file. You can also experiment with different GPT-3 engines and settings to improve the responses.


