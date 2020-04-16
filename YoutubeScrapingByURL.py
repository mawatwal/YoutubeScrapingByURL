from bs4 import BeautifulSoup 
import requests, json, os
url = input('https://www.youtube.com/watch?v=v_ol2WeNXps') 
video = {}
link = url
source = requests.get('https://www.youtube.com/watch?v=v_ol2WeNXps').text
soup = BeautifulSoup(source,'lxml')
div = soup.findAll('div')
title = div[1].find('span', class_='watch-title').text.strip() 
video['Title'] = title
channel_name = div[1].find('a', class_="yt-uix-sessionlink spf-link").text.strip()  
video['Channel']=channel_name
channel_link = ('www.youtube.com'+div[1].find('a', class_="yt-uix-sessionlink spf-link").get('href'))   
video['Channel_link'] = channel_link
subscribers = div[1].find('span', class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").text.strip()
video['Channel_subscribers'] = subscribers
view_count = div[1].find(class_= 'watch-view-count')
view_count = view_count.text.strip().split()[0]
video['Views'] = view_count
likes = div[1].find('button', class_="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-unclicked yt-uix-clickcard-target yt-uix-tooltip" ).text.strip()
video['Likes']=likes
dislikes = div[1].find('button', class_="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-unclicked yt-uix-clickcard-target yt-uix-tooltip" ).text.strip()
video['Dislikes']=dislikes
related_videos = div[1].findAll('a', class_='content-link spf-link yt-uix-sessionlink spf-link')
title_related = []
link_related = []
for i in range(len(related_videos)):
    title_related.append(related_videos[i].get('title'))
    link_related.append(related_videos[i].get('href'))
related_dictionary = dict(zip(title_related, link_related))    
video['Related_vids'] = related_dictionary
with open('YoutubeScrapingByURL.json', 'w', encoding='utf8') as ou:
    json.dump(video, ou, ensure_ascii = False)