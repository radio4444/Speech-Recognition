import speech_recognition as sr

r = sr.Recognizer()

# Capture data from a file
harvard = sr.AudioFile('Audio File/Tanzil Ehsan Intro.wav')
with harvard as source:  # read and store in source
	audio = r.record(source)  # records the data from the entire file into AudioData instance.

# print(type(audio)) | Output: <class 'speech_recognition.audio.AudioData'>

print(r.recognize_google(audio))


