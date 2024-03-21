import os

files = os.listdir("media/lambani_predicted_without_mod")

for file in files:
    splits = file.split("_")
    os.rename("media/lambani_predicted_without_mod/" + file, "media/lambani_predicted_without_mod/" + splits[0] + ".wav")