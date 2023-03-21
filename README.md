# naversia-alexa

This is a Python code for a voice assistant that responds to voice commands given by the user. The voice assistant uses several libraries such as speech_recognition, pyttsx3, pywhatkit, datetime, and wikipedia.

Functionality:
The voice assistant listens to the user's voice commands using the microphone and converts the audio to text using Google's speech recognition API. It recognizes the user's voice commands by looking for a specific trigger word, which is "Alex" in this case. The voice assistant can respond to three types of voice commands:

    "Play": If the user's command includes the word "play," the voice assistant plays the requested song on YouTube using the pywhatkit library.
    "Time": If the user's command includes the word "time," the voice assistant responds with the current time.
    "Who is": If the user's command includes the phrase "who is," the voice assistant responds with a brief summary of the requested person's Wikipedia page.

Libraries used:

    SpeechRecognition: An open-source library that provides speech recognition capabilities to Python.
    pyttsx3: A Python library that enables text-to-speech conversion.
    pywhatkit: A Python library that can play a song on YouTube using a keyword search.
    datetime: A Python library that provides date and time-related functions.
    wikipedia: A Python library that enables access to Wikipedia pages.

Instructions:

    Install the required libraries by running the following commands:
    pip install speechrecognition
    pip install pyttsx3
    pip install pywhatkit
    pip install wikipedia

    Run the code in a Python environment such as Jupyter Notebook or PyCharm.

    Once the code is running, the user can give voice commands by saying "Alex" followed by the specific command.

    The voice assistant will respond to the user's command by either playing a song on YouTube, providing the current time, or providing a brief summary of a Wikipedia page.
