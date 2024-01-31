import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

# print(mic.list_microphone_names())

# for name in mic.list_microphone_names():
# 	print(name)
try:
	with mic as source:
		# r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	print(r.recognize_google(audio))  # Sentence is fine but not when it comes to name

except sr.UnknownValueError:
	print("Speech Recognition could not understand audio")
except Exception as e:
	print(f"An unexpected error occurred: {e}")

