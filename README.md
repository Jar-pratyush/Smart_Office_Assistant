# Smart_Office_Assistant

A simple office assistant that generates professional email replies using a Large Language Model (LLM) powered by the Groq API.

---

## Features

- Collects incoming email text from the user.
- Allows specifying key bullet points to include in the reply.
- Supports choosing a reply tone: formal, friendly, concise, or detailed.
- Constructs a well-formatted prompt for the Groq LLM.
- Sends the prompt to the Groq API and displays the drafted reply.
- Supports API key management through environment variables.

---

## Installation

Make sure you have Python 3.x installed.

Install required dependencies:
---

## Usage

1. Clone the repository:
git clone https://github.com/Jar-pratyush/Smart_Office_Assistant.git

cd Smart_Office_Assistant

2. Store your Groq API key in a `.env` file in the project root:
GROQ_API_KEY=your_groq_api_key_here

3. Run the script:
python main.py

4. Follow the interactive prompts:
- Paste or type the incoming email text.
- Enter bullet points as comma-separated values.
- Choose the tone for the reply by entering 1-4.

The script will generate and display the drafted email reply.

---

## Environment Variables

- `GROQ_API_KEY`: Your API key for authenticating requests to the Groq LLM API. Must be set in a `.env` file or your shell environment.

---

## Contributing

Contributions and improvements are welcome. Feel free to submit pull requests or open issues for feature requests and bugs.

---

## License

This project is licensed under the MIT License.

---





