from moviepy.editor import *


def CreateTextedVideo(alarm_voice_path, yazi):

    video = VideoFileClip(BASE_VIDEO)
    duration = AudioFileClip(alarm_voice_path).duration
    base_alarm_audio = AudioFileClip(ALARM_MUSIC).subclip(0, duration)
    alarm_voice_audio = AudioFileClip(alarm_voice_path).subclip(0, duration)

    final_audio = CompositeAudioClip([base_alarm_audio, alarm_voice_audio])

    # Make the text. Many more options are available.
    txt_clip = TextClip(yazi, fontsize=80,
                        color='black').set_position("center")

    result = CompositeVideoClip([video, txt_clip])
    result = result.set_audio(final_audio)
    result.duration = duration

    result.write_videofile(alarm_voice_path.replace("mp3", "mp4"), fps=25)








BASE_VIDEO = "base_video.mp4"
ALARM_MUSIC = "alarm.mp3"
CreateTextedVideo(f"sümeyye_kız.mp3", i)






