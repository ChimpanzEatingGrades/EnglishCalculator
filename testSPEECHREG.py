import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something: ")
    audio = r.listen(source, phrase_time_limit=3)

    try:
        text = r.recognize_google(audio)
        print("You said: {}" .format(text))
    except:
        print("Sorry, I could not understand.")


