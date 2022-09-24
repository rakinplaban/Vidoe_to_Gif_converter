# import requests
# from bs4 import BeautifulSoup as bfs
from moviepy.editor import VideoFileClip

# r = requests.get('https://www.linkedin.com/feed/').text

# s = bfs(r,'lxml')

# print(s.prettify())

video_clip = VideoFileClip("D:/Inflack files/AI Intern/Videos/demo.mp4")
video_clip.write_gif('demo.gif')