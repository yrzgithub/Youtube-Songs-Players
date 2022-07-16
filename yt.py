from pywhatkit import playonyt
from pafy import new
from vlc import Instance

instance = Instance()
player = instance.media_player_new()

while True:
    song = input("Enter the song : ")
    if song=="" or song.isspace():
        break
    url = playonyt(song,open_video=False)

    print(f"playing song from {url}")

    pafy_obj = new(url)
    audio = pafy_obj.getbestaudio()
    stream_url = audio.url

    media = instance.media_new(stream_url)
    player.set_media(media)
    player.play()

print("Music player stopped...")