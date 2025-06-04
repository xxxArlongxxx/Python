import speech_recognition as sr


# Inicializa o reconhecedor
recognizer = sr.Recognizer()

# Usa o microfone como fonte
with sr.Microphone() as source:
    print("Fale algo, Lorde Soberano:")
    audio = recognizer.listen(source)

# Tenta reconhecer o áudio com Google
try:
    texto = recognizer.recognize_google(audio)  # type: ignore
    print("Você disse:", texto)
except sr.UnknownValueError:
    print("Não consegui entender o que foi dito.")
except sr.RequestError as e:
    print("Erro ao se comunicar com o serviço:", e)