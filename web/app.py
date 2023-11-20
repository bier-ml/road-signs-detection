import streamlit as st


def run_server():
    st.set_page_config(layout="wide")

    st.title("Road signs detection app")
    st.subheader("Upload video")

    col1, col2, col3 = st.columns(3, gap='large')

    with col1:
        text_input = st.text_input("Enter video url:", placeholder='url')


if __name__ == "__main__":
    run_server()
