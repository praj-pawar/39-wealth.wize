import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import os
import webbrowser
import chunkify

import speech2text
st.set_page_config(page_title='wealth.wize', page_icon="💸", layout="wide")

with st.sidebar:
    st.subheader("here's a gist of what you can do")
    st.write("- query about the equities market through text/voice")
    st.write("- retrieve info from credible sources through text/voice")
    st.header("")
    st.header("")
    st.subheader("souces of information")
    url1 = "https://nsdl.co.in/downloadables/pdf/SEBI%20Booklet.pdf"
    if st.button('sebi'):
        webbrowser.open_new_tab(url1)
    url2 = "https://zerodha.com/varsity/modules/"
    url3 = "https://www.bseindia.com/"
    if st.button('bse'):
        webbrowser.open_new_tab(url3)
    if st.button('zerodha varsity'):
        webbrowser.open_new_tab(url2)

    st.header("")
    st.header("")

    st.subheader("invest wizely 💸")
    st.write("deGen.ai")


st.title('wealth.wize 💸')

st.markdown("""
    <span style="font-size:30px">
    what do you want to know about the markets today?
    </span>
    """, unsafe_allow_html=True)

st.header("")

lang = ["en-IN", "te-IN", "kn-IN", "hi-IN",
        "ta-IN", "mr-IN", "ml-IN", "gu-IN", "bn-IN"]
l = st.selectbox("choose your preferred language", lang)

text_input = ""
if l == "en-IN":
    text_input = st.text_input("")
    if st.button("ask!"):
        # send data to query engine
        st.write("Here's the answer\n:", text_input)


def my_function():
    st.write("listening...")
    text = speech2text.extract_audio(l)
    st.write(text)


if st.button("talk to me!"):
    my_function()


# Display the video file
query = False
# model takes input, spits output

# this is ans of model
if st.button("Ans obtained"):
    query = True

if query:
    ans = st.success("Here's your answer")
    x = 1
    # function to generate video
    video_file = open("vid{fname}.mp4".format(fname=x), 'rb')
    video_bytes = video_file.read()
    st.video(video_file)
    status = st.radio("Do you wish to continue?", ("Yes", "No"))
    if status == 'Yes':
        st.write("Call")
        # calling query engine
    else:
        st.write("Thanks for your time. Invest wizzely")
