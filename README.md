# IBM-Watson-Generative-AI
Repo For IBM AI Analyst Certification Course and other Generative AI Projects


# Desktop Assistant

This Python script is a basic desktop assistant with speech recognition and integration with various APIs and services. The assistant interacts with the user through speech and provides responses using text-to-speech.

## Features

The desktop assistant comes with the following features:

1. **Website Navigation**: Open popular websites with a voice command. Ask the assistant to open websites like YouTube, Google, Wikipedia, etc.

2. **Time Display**: Get the current time by asking the assistant, "What's the time?"

3. **Artificial Intelligence Responses**: The assistant uses OpenAI's GPT-3.5 model to provide AI-generated responses. Ask it questions related to "Artificial Intelligence" to get informative answers.

4. **News Headlines**: Stay updated with the latest sports headlines from India. Ask for "news" or "headlines," and the assistant will fetch and read them out to you.

5. **Conversational Mode**: Engage in a conversation with the assistant. It keeps track of the conversation history and provides context-aware responses.

6. **Stop Talking and Reset Chat**: End the conversation by telling the assistant to "stop talking." You can also reset the chat history with the command "reset chat."

## Requirements

To run the desktop assistant, you will need the following:

1. Python 3.x installed on your system.
2. Required Python packages installed (use `pip install -r requirements.txt` to install them).
3. Environment variables set in a `.env` file:
   - `OPENAI_API_KEY`: API key for the OpenAI GPT-3.5 model.
   - `NEWS_API_KEY`: API key for accessing the News API.

## Limitations

The text-to-speech functionality (win32com.client) is designed for Windows systems. If you want to run the script on other platforms, you'll need to modify the text-to-speech implementation accordingly.

# Certificate:
![image](https://github.com/AdSattikar/IBM-Watson-Generative-AI/assets/78402053/17f2ea48-234e-4b6d-a826-16e6bdb67bcb)