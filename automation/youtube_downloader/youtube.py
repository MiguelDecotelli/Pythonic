from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print(f"Title: {yt.title}")

print(f"Views: {yt.views}")

yd = yt.streams.get_highest_resolution()

yd.download("/home/jagga/Vídeos/YouTube")