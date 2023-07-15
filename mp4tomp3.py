from moviepy.editor import *
import glob


def convert_video_erkek(video_path):
    video = VideoFileClip(video_path)
    video_path = video_path[4:]
    harf = video_path.split("/")[-1][0]
    if harf.upper() == "A":
        video.audio.write_audiofile("mp3/Erkek/" + "A/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "B":
        video.audio.write_audiofile("mp3/Erkek/" + "B/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "C" or harf.upper() == "Ç":
        video.audio.write_audiofile("mp3/Erkek/" + "C-Ç/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "D" or harf.upper() == "E":
        video.audio.write_audiofile("mp3/Erkek/" + "D-E/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "F" or harf.upper() == "G":
        video.audio.write_audiofile("mp3/Erkek/" + "F-G/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "H" or harf.upper() == "I" or harf.upper() == "İ":
        video.audio.write_audiofile("mp3/Erkek/" + "H-İ/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "K" or harf.upper() == "L":
        video.audio.write_audiofile("mp3/Erkek/" + "K-L/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "M":
        video.audio.write_audiofile("mp3/Erkek/" + "M/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "N":
        video.audio.write_audiofile("mp3/Erkek/" + "N/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "O" or harf.upper() == "Ö":
        video.audio.write_audiofile("mp3/Erkek/" + "O-Ö/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "P" or harf.upper() == "R":
        video.audio.write_audiofile("mp3/Erkek/" + "P-R/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "S" or harf.upper() == "Ş":
        video.audio.write_audiofile("mp3/Erkek/" + "S-Ş/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "T" or harf.upper() == "U" or harf.upper() == "Ü":
        video.audio.write_audiofile("mp3/Erkek/" + "T-Ü/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "V" or harf.upper() == "Y" or harf.upper() == "Z":
        video.audio.write_audiofile("mp3/Erkek/" + "V-Z/" + video_path.replace(".mp4",".mp3"))


def convert_video_kiz(video_path):
    video = VideoFileClip(video_path)
    video_path = video_path[4:]
    harf = video_path.split("/")[-1][0]
    if harf.upper() == "A":
        video.audio.write_audiofile("mp3/Kız/" + "A/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "B":
        video.audio.write_audiofile("mp3/Kız/" + "B/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "C" or harf.upper() == "Ç":
        video.audio.write_audiofile("mp3/Kız/" + "C-Ç/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "D" or harf.upper() == "E":
        video.audio.write_audiofile("mp3/Kız/" + "D-E/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "F" or harf.upper() == "G":
        video.audio.write_audiofile("mp3/Kız/" + "F-G/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "H" or harf.upper() == "I" or harf.upper() == "İ" or harf.upper() == "J":
        video.audio.write_audiofile("mp3/Kız/" + "H-J/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "K" or harf.upper() == "L":
        video.audio.write_audiofile("mp3/Kız/" + "K-L/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "M":
        video.audio.write_audiofile("mp3/Kız/" + "M/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "N":
        video.audio.write_audiofile("mp3/Kız/" + "N/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "O" or harf.upper() == "Ö" or harf.upper() == "P" or harf.upper() == "R":
        video.audio.write_audiofile("mp3/Kız/" + "O-R/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "S":
        video.audio.write_audiofile("mp3/Kız/" + "S/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "Ş" or harf.upper() == "T":
        video.audio.write_audiofile("mp3/Kız/" + "Ş-T/" + video_path.replace(".mp4",".mp3"))
    if harf.upper() == "Ü" or harf.upper() == "V" or harf.upper() == "Y" or harf.upper() == "Z":
        video.audio.write_audiofile("mp3/Kız/" + "Ü-Z/" + video_path.replace(".mp4",".mp3"))

files = glob.glob("mp4/*.mp4")

for f_path in files:
    if "erkekşl"  in f_path:

        convert_video_erkek(f_path)
        print(f_path + " done.")
    elif "kiz" in f_path:

        convert_video_kiz(f_path)
        print(f_path + " done.")