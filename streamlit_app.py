import requests
import streamlit as st

from audio_recorder_streamlit import audio_recorder


def post_to_language_detection_api(audio: bytes):
    return requests.post(
        url="http://localhost:8000/v1/language",
        headers={
            "Content-Type": "application/json",
            "X-API-KEY": "08e869be-8f84-450c-a775-954c91c0581a"
        },
        data={
            "file": audio
        },
    )


st.set_page_config(
    page_title="Language Detector",
    page_icon="favicon.png",
)

st.markdown("# Language Detector app")

col1, col2 = st.columns(2)

with col1:
    st.markdown("## Record an audio")
    st.markdown("Press the button to start recording")
    if audio_bytes := audio_recorder():
        st.audio(audio_bytes, format="audio/wav")
        if st.button("Detect the language"):
            res = post_to_language_detection_api(audio_bytes)
            st.write(f"Language detected => {res.json()['language']}")
            st.write(f"Status code => {res.status_code}")

with col2:
    st.markdown("## Upload an audio file")
    st.markdown("Drag and drop a .wav file here to guess the language")
    wav_file = st.file_uploader(label="Audio File", type=".wav")
    if wav_file is not None:
        bytes_value = wav_file.getvalue()
        res = post_to_language_detection_api(bytes_value)
        st.write(f"Language detected => {res.json()['language']}")
        st.write(f"Status code => {res.status_code}")
