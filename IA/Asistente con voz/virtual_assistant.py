'''
    Description:
    Create your own virtual assistant with Python.

    Author: AlejandroV
    Version: 2.0
    Video: https://youtu.be/Cr9O31eqXuA
'''

'''
El programa utiliza una librería para procesar la voz y otro para hablar
- No está implementado busqueda en google (No hecho)
- Puse limite en el while de <= 6 
- Funcion de creadores
- Funcion documentacion python
'''
import pickle

import AVMSpeechMath as sm
import AVMYT as yt
import spoty
import speech_recognition as sr
import pyttsx3
import pywhatkit
import json
from datetime import datetime, date, timedelta
import wikipedia
import pyjokes
from time import time
import webbrowser

start_time = time()
engine = pyttsx3.init()

# name of the virtual assistant
name = 'alexa'
attemts = 0

# keys
with open('src/keys.json') as json_file:
    keys = json.load(json_file)

# colors
green_color = "\033[1;32;40m"
red_color = "\033[1;31;40m"
normal_color = "\033[0;37;40m"

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

day_es = [line.rstrip('\n') for line in open('src/day/day_es.txt')]
day_en = [line.rstrip('\n') for line in open('src/day/day_en.txt')]


# def json(data):
#     fileName = 'data.json'
#     jsonString = {"data" : (data)}

#     with open(fileName, "wb") as fl:
#         pickle.dump(jsonString, fl)
#         fl.close()

def iterateDays(now):
    for i in range(len(day_en)):
        if day_en[i] in now:
            now = now.replace(day_en[i], day_es[i])
    return now

def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return iterateDays(now)

def getDaysAgo(rec):
    value =""
    if 'ayer' in rec:
        days = 1
        value = 'ayer'
    elif 'antier' in rec:
        days = 2
        value = 'antier'
    else:
        rec = rec.replace(",","")
        rec = rec.split()
        days = 0

        for i in range(len(rec)):
            try:
                days = float(rec[i])
                break
            except:
                pass
    
    if days != 0:
        try:
            now = date.today() - timedelta(days=days)
            now = now.strftime("%A, %d de %B del %Y").lower()

            if value != "":
                return f"{value} fue {iterateDays(now)}"
            else:
                return f"Hace {days} días fue {iterateDays(now)}"
        except:
            return "Aún no existíamos"
    else:
        return "No entendí"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    status = False

    with sr.Microphone() as source:
        print(f"{green_color}({attemts}) Escuchando...{normal_color}")
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
            
            if name in rec:
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True
            else:
                print(f"Vuelve a intentarlo, no reconozco: {rec}")
        except:
            pass
    return {'text':rec, 'status':status}

while attemts <= 6:
    rec_json = get_audio()

    rec = rec_json['text']
    status = rec_json['status']
    print(rec)
    if status:
        if 'estas ahi' in rec:
            speak('Por supuesto')
        
        
        elif 'reproduce' in rec:
            if 'spotify' in rec:
                music = rec.replace('reproduce en spotify', '')
                speak(f'Reproduciendo {music}')
                spoty.play(keys["spoty_client_id"], keys["spoty_client_secret"], music)
            else:
                music = rec.replace('reproduce', '')
                speak(f'Reproduciendo {music}')
                pywhatkit.playonyt(music)
                # yt.play(music)

        elif 'cuantos suscriptores tiene' in rec:
            name_subs = rec.replace('cuantos suscriptores tiene', '')
            
            speak("Procesando...")
            while True:
                try:
                    channel = yt.getChannelInfo(name_subs)
                    speak(channel["name"] + " tiene " + channel["subs"])
                    break
                except:
                    speak("Volviendo a intentar...")
                    continue

        elif 'que' in rec:
            if 'hora' in rec:
                hora = datetime.now().strftime('%I:%M %p')
                speak(f"Son las {hora}")

            elif 'dia' in rec:
                if 'fue' in rec:
                    speak(f"{getDaysAgo(rec)}")
                    data = (f"{getDaysAgo(rec)}")
                else:
                    speak(f"Hoy es {getDay()}")
                    data = (f"Hoy es {getDay()}")

        elif 'busca' in rec:
            order = rec.replace('busca', '')
            wikipedia.set_lang("es")
            info = wikipedia.summary(order, 1)
            data = info
            speak(info)
            # print(info) en info se encuentra toda la informacion que va a decir

        elif 'chiste' in rec:
            chiste = pyjokes.get_joke("es")
            speak(chiste)
            data = chiste

        elif 'cuanto es' in rec:
            speak(sm.getResult(rec))
            data = sm.getResult(rec)
            
        elif 'creadores' in rec:
            speak('Implementado por Julian, Uciel y Lucas')
            
        elif 'python' in rec:
            webbrowser.open('https://docs.python.org/3/')
            data = 'https://docs.python.org/3/'
            
        elif ('descansa' or 'salir') in rec:
            speak("Saliendo...")
            break

        else:
            print(f"Vuelve a intentarlo, no reconozco: {rec}")
        
        attemts = 0
    else:
        attemts += 1
        



print(f"{red_color} PROGRAMA FINALIZADO CON UNA DURACIÓN DE: { int(time() - start_time) } SEGUNDOS {normal_color}")