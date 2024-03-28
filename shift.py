import os
import json

# files = os.listdir("media/lambani_predicted_without_mod")

# for file in files:
#     splits = file.split("_")
#     os.rename("media/lambani_predicted_without_mod/" + file, "media/lambani_predicted_without_mod/" + splits[0] + ".wav")

# with open("D:\S2ST\Language Translation Feedback\/translations\eng-lmn\output_test_source.txt", "r", encoding="utf8") as f1:
#     lines = f1.readlines()

# with open("D:\S2ST\Language Translation Feedback\english_kannada.txt", "r", encoding="utf8") as f1:
#     english_kannada = f1.readlines()

# temp = dict()
# for sentence in english_kannada:
#     splits = sentence.split("|")
# print(len(english_kannada))
# print(len(lines))
# with open("kannada.txt", "w", encoding="utf8") as f1:
#     for line in lines:
#         line = line.split("\n")[0]
#         flag = False
#         for sentence in english_kannada:
#             splits = sentence.split("|")
#             if len(splits) == 2:
#                 kannada = splits[1]
#                 english_front = splits[0].lower()
#                 if line in english_front:
#                     # print("inside")
#                     f1.write(kannada)
#                     flag = True
#                     break
#         if not flag:
#             f1.write("\n")

def results(json_file, data_file):
    with open("static/" + data_file + ".csv", "r", encoding="utf8") as f1:
        lines = f1.readlines()
    number_of_lines = len(lines)
    print(number_of_lines)
    # print(lines[292])
    feedbacks = dict()
    f = open("media/" + json_file + ".json")
    loaded_json = json.load(f)

    for feedback in loaded_json["users"]:
        print(feedback)
        for key, val in feedback.items():
            if key != "average_text_rating" and key != "average_audio_rating":
                key_splits = key.split("_")
                # print(int(float(key_splits[1])))
                line_number = int(float(key_splits[1])) + 1
                if line_number not in feedbacks.keys():
                    empty_list = []
                    data_file_splits = lines[line_number].split("|")
                    for data_file_split in data_file_splits:
                        empty_list.append(data_file_split)
                    empty_list.append([])
                    feedbacks[line_number] = tuple(empty_list)
                feedbacks[line_number][-1].append(val)
    
    with open(json_file + "Results.json", 'w', encoding="utf8") as f1:
            json.dump(feedbacks, f1, ensure_ascii=False)

results("text", "dataText")
results("audio", "dataAudio")
results("Kannada_Lambani", "dataKannadaLambani")
results("Lambani_Kannada", "dataLambaniKannada")