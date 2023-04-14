from pytube import YouTube
from moviepy.editor import *
import os, ffmpeg, subprocess


class Ui:
    def __init__(self):
        self.link = "https://www.youtube.com/watch?v=O1OTWCd40bc"
        self.yt = YouTube(self.link)

    def start(self):
        print("Hello, welcome to the Pytube youtube downloader!")

        while True:
            print("1 - Download from YouTube")
            print("0 - Exit")
            option = int(input("Option:\n"))
            if option == 1:
                self.link = input("Please provide a link:\n")
                if YouTube(self.link):
                    self.yt = YouTube(self.link)
                    print("The link is valid!")
                else:
                    print("The link is not valid!")
                    break
                self.video_options()
            elif option == 0:
                break

    def video_options(self):
        while True:
            print("1 - Download audio only")
            print("2 - Download 720p video")
            print("3 - Download 1080p video")
            print("0 - Exit")
            option = int(input("Option:\n"))
            if option == 1:
                self.audio_only()
            elif option == 2:
                self.video()
            else:
                break

    def audio_only(self):

        audio = self.yt.streams.get_by_itag(140)
        output = audio.download()

        base, ext = os.path.splitext(output)
        file = base + '.mp3'
        os.rename(output, file)

        print(self.yt.title + " has been downloaded successfully!")

    def video(self):
        video = self.yt.streams.get_by_itag(22)
        video.download()
        print(self.yt.title + " has been downloaded successfully!")

ui = Ui()
ui.start()