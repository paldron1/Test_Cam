import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

# A simple transformer to return the original frame from webcam
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")

st.title("Simple Webcam App")

# Start the webcam stream
webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

st.write("This app captures the live webcam stream and displays it here.")
