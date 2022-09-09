import requests
import streamlit as st


url = "https://imdb8.p.rapidapi.com/title/find"

title = st.text_input('Movie title', 'The Woman King')

st.write('The current movie title is', title)

querystring = {"q": title}

headers = {
	"X-RapidAPI-Key": "31ae5e6e6cmsh430a4deebf3ea59p1b3b61jsnbb03569553ec",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

arr = response.text.split(',');
st.write(arr)
