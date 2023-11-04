import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import os
import a2t
st.set_page_config(page_title='wealth.wize', page_icon="🖖")


st.title('wealth.wize')
text_input = st.text_input("What do you want to know about the markets today?")


if st.button("Ask!"):

    st.write("Here's the answer\n:", text_input)


def my_function():
    st.write("Listening...")
    text = a2t.extract_audio()
    st.write(text)


if st.button("Talk to me..."):
    my_function()


# Display the video file
query = False
# model takes input, spits output

# query = True

# a = ['a', 'b', 'c']
# c = st.selectbox("choose", a)
# st.write("you selected {}".format, c)

if st.button("Ans obtained"):
    query = True

if query:
    ans = st.success("Here's your answer")
    x = 0
    # function to generate video
    video_file = open("output{fname}".format(fname=x), 'rb')
    video_bytes = video_file.read()
    st.video(video_file)
    status = st.radio("Do you wish to continue?", ("Yes", "No"))
    if status == 'Yes':
        st.write("Call")
        # calling query engine
    else:
        st.write("Thanks for your time. Invest wizelyy")
