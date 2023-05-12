import speech_recognition as sr
import pyttsx3
import datetime
from translate import Translator
import openai
import pywhatkit
import pyautogui
import pyaudio

audio = sr.Recognizer()
maquina = pyttsx3.init()
openai.api_key = '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'  # Substitua 'SUA_API_KEY' pela sua chave de API do OpenAI

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'gpt' in comando:
                comando = comando.replace('gpt', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando

def obter_resposta(pergunta):
    openai_prompt = f"Q: {pergunta}\nA:"
    resposta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=openai_prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )
    return resposta.choices[0].text.strip()

def traduzir_texto(texto, origem, destino):
    translator = Translator(from_lang=origem, to_lang=destino)
    return translator.translate(texto)

def comando_voz_usuario():
    comando = executa_comando()
    if 'hora' in comando:
        hora = datetime.datetime.now().strftime('%H:%M:%S')  # Modificado para retornar hora no formato 24 horas
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()
    elif 'o que é' in comando:
        pergunta = comando.replace('o que é', '')
        pergunta = pergunta.strip()
        resposta = obter_resposta(pergunta)
        resposta_traduzida = traduzir_texto(resposta, 'en', 'pt')
        print(resposta_traduzida)
        maquina.say(resposta_traduzida)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()
    elif 'abra o' in comando:
        app = comando.replace('abra o', '').strip()
        maquina.say(f"Abrindo {app}")
        maquina.runAndWait()
        pyautogui.press('winleft')
        pyautogui.typewrite(app)
        pyautogui.press('enter')


comando_voz_usuario()
