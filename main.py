import os
from os import startfile

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'tina' in comando:
                comando = comando.replace('tina', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Seu mic não está funcionando')

    return comando


def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()

    elif 'chrome' in comando:
        abrir = comando.replace('chrome', '')
        resultado = startfile('chrome.exe')
        maquina.say('Abrindo chrome')
        maquina.runAndWait()

    elif 'github' in comando:
        abrir = comando.replace('github','')
        resultado = startfile('https://github.com/magalhaes13')
        maquina.say('Abrindo GitHub')
        maquina.runAndWait()

    elif 'banco de dados' in comando:
        abrir = comando.replace('bando de dados','')
        resultado = startfile('C:\Program Files\MySQL\MySQL Workbench 8.0\MySQLWorkbench.exe')
        maquina.say('Abrindo bd')
        maquina.runAndWait()




comando_voz_usuario()