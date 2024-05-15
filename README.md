# Voice_Activated_personalassitant_using_tkinter
A Python-based voice-activated personal assistant application utilizing speech recognition, text-to-speech, and various automated tasks such as opening websites, playing music, and setting alarms. Built with Tkinter for the GUI, Pyttsx3 for text-to-speech, and SpeechRecognition for voice commands
Features:
Voice Recognition: Uses speech_recognition to understand and process voice commands.
Text-to-Speech: Utilizes pyttsx3 for converting text responses to speech.
GUI Interface: Built with Tkinter, providing a user-friendly interface.
Automated Tasks: Includes functionalities like opening websites (YouTube, Google), playing music, setting alarms, and providing the current time.
Customizable Alarms: Set alarms using voice commands, with options for AM/PM.
Music Player: Play specific audio files upon certain commands.

Dependencies:
tkinter: For the GUI interface.
Pillow: For image processing.
pyttsx3: For text-to-speech conversion.
speech_recognition: For recognizing voice commands.
wikipedia: For fetching summaries from Wikipedia.
webbrowser: For opening web pages.
pygame: For playing music.
smtplib: For sending emails (optional, not fully implemented).


How to Run:


Clone the repository:
git clone https://github.com/yourusername/Voice-Activated-Personal-Assistant.git
cd Voice-Activated-Personal-Assistant


Install Dependencies:
Ensure you have Python installed. Install the required Python packages using pip:
pip install -r requirements.txt


Run the Application:
python main.py

