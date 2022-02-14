import streamlit as st
import pygame
st.set_page_config(page_title="Happy Valentines Day",layout="centered")
col1,col2 = st.columns([1,1])
with col1:
    st.image("images1.png")
with col2:
    st.header(" ")
    st.header(" ")
    st.header(" ")
    if st.button("Press the Button"):
        for i in range(5):
            st.balloons()
            st.balloons()
        pygm = pygame.mixer.init()
        pygm.mixer.music.load("Welcome.MP3")
        pygm.mixer.music.play(loops=2)
        st.write("<p style = 'color:Red; font-weight: bold'> Happy Valentine Day Baby  😍 </p>",unsafe_allow_html=True)
        st.write("Yeh Apka phla gift "
                 "Apke ke liye ek choti se video bhi bnai h maine khud niche ek or button use press krtey hi apko show hogi")
Date = st.date_input("Btao hum phli bar maine apko kb propose kiya the Date")
if st.button("submit"):
    if str(Date) == "2021-10-29":
            st.video("mai.mp4")


