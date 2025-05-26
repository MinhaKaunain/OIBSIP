import tkinter as tk
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import threading

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    output_text.insert(tk.END, "Assistant: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your AI Assistant. How can I help you?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            user_input.insert(tk.END, command)
            process_command(command.lower())
        except sr.UnknownValueError:
            speak("Sorry, I could not understand. Please try again.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")

def process_command(command):
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "exit" in command or "close" in command:
        speak("Goodbye!")
        root.destroy()

    else:
        speak("Sorry, I didn't understand that command.")

def start_listening():
    thread = threading.Thread(target=listen)
    thread.start()

# GUI Setup
root = tk.Tk()
root.title("AI Voice Assistant")
root.geometry("500x400")

output_text = tk.Text(root, height=15, width=60)
output_text.pack(pady=10)

user_input = tk.Entry(root, width=60)
user_input.pack(pady=10)

speak_button = tk.Button(root, text="Speak", command=start_listening)
speak_button.pack()

wish()
root.mainloop()
