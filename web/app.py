import streamlit as st


def run_server():
    st.set_page_config(layout="wide")

    st.title("Road signs detection app")
    video_file = st.file_uploader('Upload a video', type=['mp4', 'avi'])

    if video_file:
        run_button = st.button('Run detection')

        if run_button:
            st.text('Processing...')


if __name__ == "__main__":
    run_server()
