import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am your assistant. How can I help you?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""

def main():
    greet()
    while True:
        command = listen()

        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {date}")

        elif "search" in command:
            speak("What should I search for?")
            query = listen()
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
