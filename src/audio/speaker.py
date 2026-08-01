import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")

# 0 = Male
# 1 = Female (if available)
engine.setProperty("voice", voices[1].id)


def speak(text):
    print(f"Evi: {text}")
    engine.say(text)
    engine.runAndWait()