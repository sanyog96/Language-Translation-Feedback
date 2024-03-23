import os

# files = os.listdir("media/lambani_predicted_without_mod")

# for file in files:
#     splits = file.split("_")
#     os.rename("media/lambani_predicted_without_mod/" + file, "media/lambani_predicted_without_mod/" + splits[0] + ".wav")

with open("D:\S2ST\Language Translation Feedback\/translations\eng-lmn\output_test_source.txt", "r", encoding="utf8") as f1:
    lines = f1.readlines()

with open("D:\S2ST\Language Translation Feedback\english_kannada.txt", "r", encoding="utf8") as f1:
    english_kannada = f1.readlines()

# temp = dict()
# for sentence in english_kannada:
#     splits = sentence.split("|")
print(len(english_kannada))
print(len(lines))
with open("kannada.txt", "w", encoding="utf8") as f1:
    for line in lines:
        line = line.split("\n")[0]
        flag = False
        for sentence in english_kannada:
            splits = sentence.split("|")
            if len(splits) == 2:
                kannada = splits[1]
                english_front = splits[0].lower()
                if line in english_front:
                    # print("inside")
                    f1.write(kannada)
                    flag = True
                    break
        if not flag:
            f1.write("\n")
