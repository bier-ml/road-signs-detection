import streamlit as st
import torch
import tempfile
from PIL import Image
import cv2


def process_video(uploaded_video):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_video.read())

    vf = cv2.VideoCapture(tfile.name)

    stframe = st.empty()
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./models/best.pt')
    model.conf = 0.6

    while vf.isOpened():
        ret, frame = vf.read()

        if frame is None:
            break
        # model expects images in RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pilimg = Image.fromarray(frame)

        results = model(pilimg, size=640)

        # rendering the processed frame
        stframe.image(results.render(), channels="RGB", width=720)

    vf.release()


def run_server():
    st.set_page_config(layout="wide")

    st.title("Road signs detection app")
    uploaded_video = st.file_uploader('Upload a video', type=['mp4', 'avi'])

    if uploaded_video:
        run_button = st.button('Run detection')

        if run_button:
            st.text('Processing...')
            process_video(uploaded_video)


if __name__ == "__main__":
    run_server()
