#############################
# IMPORTING LIBRARIES
#############################
import os
import time
import youtube_dl
import json

config = {}

#############################
# FUNCTION: GREETING
#############################


def greeting():
    print("""
   _____ __________________   _________                                   __   
  /     \|______   \_____  \  \_   ___ \  ____   _______  __ ____________/  |_ 
 /  \ /  \|     ___/ _(__  <  /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __|
/    Y    \    |    /       \ \     \___(  <_> )   |  \   /\  ___/|  | \/|  |  
\____|__  /____|   /______  /  \______  /\____/|___|  /\_/  \___  >__|   |__|  
        \/                \/          \/            \/          \/             
    """)


#############################
# FUNCTION: DOWNLOAD SONG
#############################

def download_song(video_url):
    try:
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
    except:
        print('Error downloading video')

#############################
# FUNCTION: CHECK FILE EXISTS
#############################


def check_file_exists(filename):
    print("Checking for file " + filename)
    if not os.path.exists(filename):
        return False
    else:
        return True

#############################
# FUNCTION: MAKE DIRECTORY
#############################


def make_directory(directory):
    print('Creating directory...')
    time.sleep(1)
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except:
        print('Failed to create directory')

#############################
# FUNCTION: LOAD JSON
#############################


def load_json(filename):
    try:
        if os.path.exists(filename):

            with open('config.json', 'r') as config_file:
                config_json = json.load(config_file)
                for key, value in config_json.items():
                    config[key] = value
    except:
        print('There was an error.')

#############################
# FUNCTION: DOWNLOAD YT VIDEO AS MP3
#############################


def download_ytvid_as_mp3():
    load_json('config.json')
    if config['songs'] and config['songs'].length > 0:
        for song in config['songs']:
            download_song(song)
    else:
        video_url = input("Please enter the URL of youtube video: ")
        if video_url:
            download_song(video_url)


greeting()
download_ytvid_as_mp3()
