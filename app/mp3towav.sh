filename=$1
mp3_filename=filename + ".mp3"
wav_filename=filename + ".wav"

ffmpeg -i mp3_filename wav_filename