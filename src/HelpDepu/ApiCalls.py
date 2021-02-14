import requests
import re  # regular expressions
import datetime
import gmaps
import gmaps.datasets
import time
import json
from monkeylearn import MonkeyLearn
from time import sleep
from google.cloud import translate_v2 as translate
from google.cloud import language_v1
from google.cloud.language_v1 import types

import os

def CallApis(text):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Usuario/SocialHackers/src/claves.json"
    #import os
    #from google.oauth2 import service_account
    texto=str(text)
    print(texto+'el texto del funcionario')
    #gmaps.configure(api_key="AIzaSyDo-i5z39is5UaVtmic0aAdenVlf33fkow")
    #credentials = service_account.Credentials.from_service_account_file("C:/Users/Usuario/claves.json")
    #client = translate.TranslateServiceClient(credentials=credentials)
    ml = MonkeyLearn('04331f53b46d850f750509ec4bf92f17b0df803a')
    translate_client = translate.Client()

    result = translate_client.translate(text, target_language='en')
    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

    texttraducido = result["translatedText"]
    
    response_type = ml.classifiers.classify(
    model_id='cl_o46qggZq',
    data=[texttraducido])
    response_sentiment = ml.classifiers.classify(
    model_id='cl_pi3C7JiL',
    data=[texttraducido])
    tag_type = response_type.body[0]['classifications'][0]['tag_name']
    tag_sentiment = response_sentiment.body[0]['classifications'][0]['tag_name']
    if tag_type == "Health & Medicine":
        return "Salud"
    elif tag_type == "Food & Drink":
        return "Comida"
    elif tag_type == "Environment" :
        return "Medio Ambiente"
    elif tag_type == "Education":
        return "Educacion"
    elif tag_type == "Society":
        return "Trabajo"
    elif tag_sentiment == "Negative":
        return "Psicologia"
    else:
        return "Others"


   

#fig = gmaps.figure()
#fig



#headers = {"Accept": "application/json", "Content-Type": "application/json"}
#text = { "text": "'+translate+'" }
#url = "https://sentim-api.herokuapp.com/api/v1/"
#response = requests.post(url, data=json.dumps(text), headers=headers)
#print(response)
#print(u"Type: {}".format(response["type"]))