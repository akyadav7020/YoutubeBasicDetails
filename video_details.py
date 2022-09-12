import time
from bs4 import BeautifulSoup as bs
import re
import requests
import json

def title_of_channel(home_link):
    """ returns channene name and unique channel_url_id for a particulal channel link"""
    try:
        html = requests.get(home_link)
        html_result = bs(html.text, "html.parser")
        data = re.search(r"var ytInitialData = ({.*?});", str(html_result.prettify())).group(1)
        json_data = json.loads(data)
        ch_name = json_data['header']['c4TabbedHeaderRenderer']['title']
        ch_url = json_data['header']['c4TabbedHeaderRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
        ch_url=ch_url.split("/")[2]
        return ch_name,ch_url
    except Exception as e:
        return "Something Wrong"

def Total_Views(id):
    """ returns Total Views on a particular Video"""
    try:
        link = link = "https://www.youtube.com/watch?v="+id
        html = requests.get(link)
        html_result = bs(html.text, "html.parser")
        views = html_result.find("meta",itemprop="interactionCount")['content']
        return int(views)
    except Exception as e:
        return "Retry"

def Total_Likes(id):
    try:
        link = link = "https://www.youtube.com/watch?v=" + id
        html = requests.get(link)
        html_result = bs(html.text, "html.parser")
        data = re.search(r"var ytInitialData = ({.*?});", str(html_result.prettify())).group(1)
        json_data = json.loads(data)
        videoPIR =json_data['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
        likes_label = videoPIR['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
        likes_str = likes_label.split(' ')[0].replace(',','')
        likes = 0 if likes_str.lower() =="no" else likes_str
        return int(likes)
    except Exception as e:
        return "Retry"
