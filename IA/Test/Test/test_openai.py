import openai
import os
from googletrans import Translator
import json

"""
INTENTAR CON VOZ
IF VOZ O TECLADO

SE PUEDE ENVIAR EN JSON TAMBIÉN
"""

# translator = Translator()

def gpt3(stext):
    openai.api_key='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'
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=stext,
    temperature=0.1,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    
    content = response.choices[0].text.split('.')
    return content

    # result = translator.translate(query, dest="en")

    
    # result2 = translator.translate(response, dest="es")