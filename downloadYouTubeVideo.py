from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=-l35Ml9PLUE")
yt = yt.get('mp4', '360p')
video.download('C:/Git_Projects2/Human-action-recognition/Videos')