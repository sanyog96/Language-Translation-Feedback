from django.shortcuts import render, redirect
import pandas as pd
import random
# from pydub import AudioSegment
from django.http import JsonResponse
import subprocess
# import ffmpeg
import sys
import json
from django.conf import settings

# Create your views here.

def evaluate(request):
    # Map the list with a key value `data`
    # users = pd.read_csv("D:\S2ST\Language Translation Feedback\static\dataText.csv", sep='|')
    users = pd.read_csv(settings.STATIC_ROOT + "dataText.csv", sep='|')
    n = users.shape[0]
    ids = random.sample(range(0, n), 10)
    items = []
    for id in ids:
        item_dict = dict()
        item_dict['id'] = id
        item_dict['english_source'] = users.iloc[id]['english_source']
        item_dict['lambani_predicted'] = users.iloc[id]['lambani_predicted']
        item_dict['lambani_target'] = users.iloc[id]['lambani_target']
        item_dict['kannada_sentence'] = users.iloc[id]['kannada_sentence']
        items.append(item_dict)

    context = {
        "datas" : items
    }
    return render(request, "evaluate.html", context)

def kannada_lambani(request):
    # Map the list with a key value `data`
    # users = pd.read_csv("D:\S2ST\Language Translation Feedback\static\dataText.csv", sep='|')
    users = pd.read_csv(settings.STATIC_ROOT + "dataKannadaLambani.csv", sep='|')
    n = users.shape[0]
    ids = random.sample(range(0, n), 10)
    items = []
    for id in ids:
        item_dict = dict()
        item_dict['id'] = id
        item_dict['kannada_source'] = users.iloc[id]['kannada_source']
        item_dict['lambani_predicted'] = users.iloc[id]['lambani_predicted']
        item_dict['lambani_target'] = users.iloc[id]['lambani_target']
        items.append(item_dict)

    context = {
        "datas" : items
    }
    return render(request, "kannada_lambani.html", context)

def lambani_kannada(request):
    # Map the list with a key value `data`
    # users = pd.read_csv("D:\S2ST\Language Translation Feedback\static\dataText.csv", sep='|')
    users = pd.read_csv(settings.STATIC_ROOT + "dataLambaniKannada.csv", sep='|')
    n = users.shape[0]
    ids = random.sample(range(0, n), 10)
    items = []
    for id in ids:
        item_dict = dict()
        item_dict['id'] = id
        item_dict['lambani_source'] = users.iloc[id]['lambani_source']
        item_dict['kannada_predicted'] = users.iloc[id]['kannada_predicted']
        item_dict['kannada_target'] = users.iloc[id]['kannada_target']
        items.append(item_dict)

    context = {
        "datas" : items
    }
    return render(request, "lambani_kannada.html", context)

def audio(request):
    # Map the list with a key value `data`
    # users = pd.read_csv("D:\S2ST\Language Translation Feedback\static\dataAudio.csv", sep='|')
    users = pd.read_csv(settings.STATIC_ROOT + "dataAudio.csv", sep='|')
    n = users.shape[0]
    ids = random.sample(range(0, n), 10)
    items = []
    for id in ids:
        item_dict = dict()
        item_dict['id'] = id
        # item_dict['english_source'] = users.iloc[id]['english_source']
        item_dict['lambani_sentence'] = users.iloc[id]['lambani_sentence']
        item_dict['lambani_truth_audio'] = "\lambani_truth\\" + str(users.iloc[id]['number']) + ".wav"
        item_dict['lambani_predicted_audio'] = "\lambani_predicted_with_mod\\" + str(users.iloc[id]['number']) + ".wav"
        items.append(item_dict)

    context = {
        "datas" : items
    }

    return render(request, "audio.html", context)

def saveText(request):
    if request.method == 'POST':
        # with open('D:\S2ST\Language Translation Feedback\media\/text.json', 'r') as f1:
        with open(settings.MEDIA_ROOT + 'text.json', 'r') as f1:
            json_object = json.load(f1)

        values_dict = {
            'option1': 1, 
            'option2': 2, 
            'option3': 3, 
            'option4': 4, 
            'option5': 5
            }
        response = request.POST.dict()
        result = dict()
        text_total = 0
        counter = 0
        for key, value in response.items():
            if key != 'csrfmiddlewaretoken':
                if 'text' in key:
                    text_total += values_dict[value]
                    counter += 1
                result[key] = values_dict[value]
        result['average_text_rating'] = float(text_total)/float(counter)
        json_object['count'] = json_object['count'] + 1
        json_object['users'].append(result)
        total_text_rating = 0
        for user in json_object['users']:
            total_text_rating += user['average_text_rating']
        items = dict()
        json_object["overall_average_text_rating"] = float(total_text_rating)/float(json_object['count'])

        # with open('D:\S2ST\Language Translation Feedback\media\/text.json', 'w') as f1:
        with open(settings.MEDIA_ROOT + 'text.json', 'w') as f1:
            json.dump(json_object, f1)
        
        items['counter'] = json_object['count']
        items["overall_average_text_rating"] = round(json_object["overall_average_text_rating"], 2)
        context = {
            "datas" : items
        }
    
    return render(request, "saveText.html", context)

def saveKannadaLambani(request):
    if request.method == 'POST':
        # with open('D:\S2ST\Language Translation Feedback\media\/text.json', 'r') as f1:
        with open(settings.MEDIA_ROOT + 'Kannada_Lambani.json', 'r') as f1:
            json_object = json.load(f1)

        values_dict = {
            'option1': 1, 
            'option2': 2, 
            'option3': 3, 
            'option4': 4, 
            'option5': 5
            }
        response = request.POST.dict()
        result = dict()
        text_total = 0
        counter = 0
        for key, value in response.items():
            if key != 'csrfmiddlewaretoken':
                if 'text' in key:
                    text_total += values_dict[value]
                    counter += 1
                result[key] = values_dict[value]
        result['average_text_rating'] = float(text_total)/float(counter)
        json_object['count'] = json_object['count'] + 1
        json_object['users'].append(result)
        total_text_rating = 0
        for user in json_object['users']:
            total_text_rating += user['average_text_rating']
        items = dict()
        json_object["overall_average_text_rating"] = float(total_text_rating)/float(json_object['count'])

        # with open('D:\S2ST\Language Translation Feedback\media\/text.json', 'w') as f1:
        with open(settings.MEDIA_ROOT + 'Kannada_Lambani.json', 'w') as f1:
            json.dump(json_object, f1)
        
        items['counter'] = json_object['count']
        items["overall_average_text_rating"] = round(json_object["overall_average_text_rating"], 2)
        context = {
            "datas" : items
        }
    
    return render(request, "saveKannadaLambani.html", context)

def saveLambaniKannada(request):
    if request.method == 'POST':
        # with open('D:\S2ST\Language Translation Feedback\media\/text.json', 'r') as f1:
        with open(settings.MEDIA_ROOT + 'Lambani_Kannada.json', 'r') as f1:
            json_object = json.load(f1)

        values_dict = {
            'option1': 1, 
            'option2': 2, 
            'option3': 3, 
            'option4': 4, 
            'option5': 5
            }
        response = request.POST.dict()
        result = dict()
        text_total = 0
        counter = 0
        for key, value in response.items():
            if key != 'csrfmiddlewaretoken':
                if 'text' in key:
                    text_total += values_dict[value]
                    counter += 1
                result[key] = values_dict[value]
        result['average_text_rating'] = float(text_total)/float(counter)
        json_object['count'] = json_object['count'] + 1
        json_object['users'].append(result)
        total_text_rating = 0
        for user in json_object['users']:
            total_text_rating += user['average_text_rating']
        items = dict()
        json_object["overall_average_text_rating"] = float(total_text_rating)/float(json_object['count'])

        # with open('D:\S2ST\Language Translation Feedback\media\/text.json', 'w') as f1:
        with open(settings.MEDIA_ROOT + 'Lambani_Kannada.json', 'w') as f1:
            json.dump(json_object, f1)
        
        items['counter'] = json_object['count']
        items["overall_average_text_rating"] = round(json_object["overall_average_text_rating"], 2)
        context = {
            "datas" : items
        }
    
    return render(request, "saveLambaniKannada.html", context)

def saveAudio(request):
    if request.method == 'POST':
        # with open('D:\S2ST\Language Translation Feedback\media\/audio.json', 'r') as f1:
        with open(settings.MEDIA_ROOT + 'audio.json', 'r') as f1:
            json_object = json.load(f1)
        values_dict = {
            'option1': 1, 
            'option2': 2, 
            'option3': 3, 
            'option4': 4, 
            'option5': 5
            }
        response = request.POST.dict()
        result = dict()
        audio_total = 0
        counter = 0
        for key, value in response.items():
            if key != 'csrfmiddlewaretoken':
                if 'audio' in key:
                    counter += 1
                    audio_total += values_dict[value]
                result[key] = values_dict[value]
        result['average_audio_rating'] = float(audio_total)/float(counter)
        json_object['count'] = json_object['count'] + 1
        json_object['users'].append(result)
        total_audio_rating = 0
        for user in json_object['users']:
            total_audio_rating += user['average_audio_rating']
        items = dict()
        json_object["overall_average_audio_rating"] = float(total_audio_rating)/float(json_object['count'])

        # with open('D:\S2ST\Language Translation Feedback\media\/audio.json', 'w') as f1:
        with open(settings.MEDIA_ROOT + 'audio.json', 'w') as f1:
            json.dump(json_object, f1)
        
        items['counter'] = json_object['count']
        items["overall_average_audio_rating"] = round(json_object["overall_average_audio_rating"], 2)
        context = {
            "datas" : items
        }
    
    return render(request, "saveAudio.html", context)

def rating(request):
    # with open('D:\S2ST\Language Translation Feedback\media\/audio.json', 'r') as f1:
    with open(settings.MEDIA_ROOT + 'audio.json', 'r') as f1:
        audio_json_object = json.load(f1)
    # with open('D:\S2ST\Language Translation Feedback\media\/text.json', 'r') as f1:
    with open(settings.MEDIA_ROOT + 'text.json', 'r') as f1:
        text_json_object = json.load(f1)
    with open(settings.MEDIA_ROOT + 'Kannada_Lambani.json', 'r') as f1:
        kannada_lambani_json_object = json.load(f1)
    with open(settings.MEDIA_ROOT + 'Lambani_Kannada.json', 'r') as f1:
        lambani_kannada_json_object = json.load(f1)
    items = dict()
    items['text_counter'] = text_json_object['count']
    items['audio_counter'] = audio_json_object['count']
    items["overall_average_text_rating"] = round(text_json_object["overall_average_text_rating"], 2)
    items["overall_average_audio_rating"] = round(audio_json_object["overall_average_audio_rating"], 2)
    items['kannada_lambani_counter'] = kannada_lambani_json_object['count']
    items["overall_average_kannada_lambani_rating"] = round(kannada_lambani_json_object["overall_average_text_rating"], 2)
    items['lambani_kannada_counter'] = lambani_kannada_json_object['count']
    items["overall_average_lambani_kannada_rating"] = round(lambani_kannada_json_object["overall_average_text_rating"], 2)
    context = {
        "datas" : items
    }
    
    return render(request, "rating.html", context)
