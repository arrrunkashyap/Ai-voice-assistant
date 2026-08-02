import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")

# Try to use a female voice if available
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)


def speak(text: str):
    print(f"EVI: {text}")
    engine.say(text)
    engine.runAndWait()