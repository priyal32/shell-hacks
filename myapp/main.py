# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import base64
import json

import pandas as pd

import streamlit as st
import requests

from AnilistPython import Anilist
anilist = Anilist()

st.title("Anime Recommendation maker")
st.subheader("Enter an Anime or Enter a genre")

title = st.text_input('anime title', 'attack on titan')
genre = st.text_input('anime genre', 'Action')

st.write('The current movie title is', title)
st.write(anilist.get_anime_from_database(title))
#st.write(anilist.search_anime(genre=['Action', 'Adventure', 'Drama'], year=[2016, 2019], score=range(80, 95)))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
