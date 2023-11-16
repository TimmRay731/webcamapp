import streamlit as st
import cv2
from datetime import datetime
st.title("Camera Detector")

start = st.button("Start Camera")


if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)
    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(img=frame, text=datetime.today().strftime("%A"), org=(10,30),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255,0,0))
        cv2.putText(img=frame, text=datetime.today().strftime("%I:%M:%S "), org=(10, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255, 255, 255))
        streamlit_image.image(frame)
