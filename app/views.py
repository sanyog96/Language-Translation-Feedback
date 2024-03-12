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

# Create a dummy list containing the data of a user as a dictionary.
users = pd.read_csv("D:\S2ST\Language Translation Feedback\static\data.csv", sep='|')
# print(users.columns)
# Create your views here.

def index(request):
    # Map the list with a key value `data`
    n = users.shape[0]
    ids = random.sample(range(0, n), 2)
    items = []
    for id in ids:
        item_dict = dict()
        item_dict['id'] = id
        item_dict['source'] = users.iloc[id]['source']
        item_dict['kannada_predicted'] = users.iloc[id]['kannada_predicted']
        item_dict['lambani_predicted'] = users.iloc[id]['lambani_predicted']
        item_dict['kannada_target'] = users.iloc[id]['kannada_target']
        item_dict['lambani_target'] = users.iloc[id]['lambani_target']
        # item_dict['kannada_audio'] = users.iloc[id]['kannada_audio']
        # kannada_sound = AudioSegment.from_mp3(users.iloc[id]['kannada_audio'])
        kannada_file_basename = users.iloc[id]['kannada_audio'].split('.')[0]
        # kannada_sound.export(kannada_file_basename + ".wav", format="wav")
        # subprocess.call(['ffmpeg', '-i', users.iloc[id]['kannada_audio'], kannada_file_basename + ".wav"])
        # subprocess.call(['C:\ffmpeg\bin\ffmpeg.exe', '-i',users.iloc[id]['kannada_audio'], kannada_file_basename + ".wav"])
        # ffmpeg.input(users.iloc[id]['kannada_audio'], pattern_type='glob').output(kannada_file_basename + ".wav").run()
        item_dict['kannada_audio'] = kannada_file_basename + ".wav"
        # item_dict['lambani_audio'] = users.iloc[id]['lambani_audio']
        # lambani_sound = AudioSegment.from_mp3(users.iloc[id]['lambani_audio'])
        lambani_file_basename = users.iloc[id]['lambani_audio'].split('.')[0]
        # lambani_sound.export(lambani_file_basename + ".wav", format="wav")
        # subprocess.call(['ffmpeg', '-i', users.iloc[id]['lambani_audio'], lambani_file_basename + ".wav"])
        # subprocess.call(['C:\ffmpeg\bin\ffmpeg.exe', '-i', users.iloc[id]['lambani_audio'], lambani_file_basename + ".wav"])
        # ffmpeg.input(users.iloc[id]['lambani_audio'], pattern_type='glob').output(lambani_file_basename + ".wav").run()
        item_dict['lambani_audio'] = lambani_file_basename + ".wav"
        # print(item_dict)
        items.append(item_dict)

    context = {
        "datas" : items
    }
    # return 
    # Pass the context along with the template
    return render(request, "index.html", context)

def post(request):
#    form = self.form_class(request.POST)
    if request.method == 'POST':
        # print(request.POST.keys())
        with open('D:\S2ST\Language Translation Feedback\media\poll.json', 'r') as f1:
            json_object = json.load(f1)
        # print(json_object)
        # print(type(request.POST.dict()))
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
        audio_total = 0
        counter = 0
        for key, value in response.items():
            if key != 'csrfmiddlewaretoken':
                if 'text' in key:
                    text_total += values_dict[value]
                    counter += 1
                if 'audio' in key:
                    audio_total += values_dict[value]
                result[key] = values_dict[value]
        result['average_text_rating'] = float(text_total)/float(counter)
        result['average_audio_rating'] = float(audio_total)/float(counter)
        # print(result)
        json_object['count'] = json_object['count'] + 1
        json_object['users'].append(result)
        total_text_rating = 0
        total_audio_rating = 0
        for user in json_object['users']:
            total_text_rating += user['average_text_rating']
            total_audio_rating += user['average_audio_rating']
        items = dict()
        json_object["overall_average_text_rating"] = float(total_text_rating)/float(json_object['count'])
        json_object["overall_average_audio_rating"] = float(total_audio_rating)/float(json_object['count'])
        with open('D:\S2ST\Language Translation Feedback\media\poll.json', 'w') as f1:
            json.dump(json_object, f1)
        items['counter'] = json_object['count']
        items["overall_average_text_rating"] = round(json_object["overall_average_text_rating"], 2)
        items["overall_average_audio_rating"] = round(json_object["overall_average_audio_rating"], 2)
        context = {
            "datas" : items
        }
    
    # print(request.POST)
    return render(request, "register.html", context)

