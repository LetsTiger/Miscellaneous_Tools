from pytube import YouTube
import os

def download(url):
    video_url = url
    yt = YouTube(video_url)

    streams = yt.streams.filter(file_extension='mp4')
    stream = streams.first()

    save_path = f"{os.getcwd()}/Download Output/"
    file_name = f'{yt.title}.mp4'

    stream.download(output_path=save_path, filename=file_name)

    print(f'YouTube Video erfolgreich in {save_path}{file_name} heruntergeladen.')