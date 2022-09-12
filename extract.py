from pytube import YouTube
import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq


def youtubescraper(id):
    try:
        link = "https://www.youtube.com/watch?v="+id
        video = YouTube(link)
        title = video.title
        videos = video.streams.filter(only_video=True,res="144p",mime_type="video/mp4")
        thumbnail_url = video.thumbnail_url
        return(link,title,thumbnail_url)
    except Exception as e:
        return "Somthing Went Wrong"

def get_id_of_videos(home_link):
    try:
        html = uReq(home_link)
        html_result = html.read().decode()
        v = re.findall(r"watch\?v=(\S{11})", html_result)
        return (v)
    except Exception as e:
        return "Somthing Went Wrong"





