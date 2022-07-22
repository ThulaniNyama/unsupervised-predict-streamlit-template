# from cgitb import html
import urllib.request
import unicodedata
import re
# from pyrsistent import v
from streamlit_player import st_player
import streamlit as st

def youtubeScrapper(top_10):
    # s = u + str(top_10)
    search_string = unicodedata.normalize('NFKD', top_10).encode('ascii', 'ignore').decode()
    st.write(search_string)
    youtube_str = re.sub("[ ]", "+", search_string)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + youtube_str+ "+trailer")
    vid_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    trailer_res = 'https://www.youtube.com/watch?v=' + vid_id[0]
    st_player(trailer_res)