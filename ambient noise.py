import speech_recognition as sr

r = sr.Recognizer()

jackhammer = sr.AudioFile('Audio File/jackhammer.wav')
with jackhammer as source:
	r.adjust_for_ambient_noise(source, duration=0.4)  # this code throws unknownError without duration<0.5
	audio = r.record(source)

print(r.recognize_google(audio, show_all=True)) # using show-all: return most likley transcription
