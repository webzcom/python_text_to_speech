import pyttsx3

engine = pyttsx3.init()

# Getting details of current speaking rate
rate = engine.getProperty('rate')
print(f"Current speech rate: {rate}")

# Setting up a new speaking rate
engine.setProperty('rate', 180)  # slower or faster based on preference

# Getting details of current volume
volume = engine.getProperty('volume')
print(f"Current volume: {volume}")

# Setting up a new volume level
engine.setProperty('volume', 0.9)  # Scale from 0.0 to 1.0

# Getting available voices
voices = engine.getProperty('voices')

for voice in voices:
    print(voice.name.lower())
# Setting a specific voice
for voice in voices:
    print(voice.name.lower())
    if 'hazel' in voice.name.lower():  # Can change "english" to any other language or gender preference
        engine.setProperty('voice', voice.id)
        break

file_path = 'readme.txt'
# Open the file and read the contents
with open(file_path, 'r') as file:
    file_contents = file.read()

engine.say(file_contents)
engine.runAndWait()
