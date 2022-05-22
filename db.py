import wikipedia
from deep_translator import GoogleTranslator
import requests
import json

from config import wiki_lang,input_lang,onput_lang,app_id,app_key


def database(text):
    wikipedia.set_lang(wiki_lang)
    try:
        messagetrans = GoogleTranslator(source='auto', target=input_lang).translate(text)
        res = wikipedia.summary(messagetrans)
        transwiki = GoogleTranslator(source='auto', target=onput_lang).translate(res)
    except:
        transwiki = f'{text} xaqida hech qanday malumot topilmadi.'

    return transwiki
def database2(text):
    language = 'en-gb'
    word_id = GoogleTranslator(source='auto',target=input_lang).translate(text)
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word_id.lower()
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    res = r.json()
    if 'error' in res.keys():
        return database(text)
    'senses'
    ontput = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for i in senses:
        t = GoogleTranslator(source='auto',target=onput_lang).translate(f"👉 {i['definitions'][0]}")
        definitions.append(t)
        ontput['definitions'] = "\n".join(definitions)
    return ontput

