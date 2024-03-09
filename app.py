import streamlit as st
import time


def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def search_and_process_in_database():
    progress_text = st.empty()
    progress_bar = st.progress(0)

    progress_text.subheader("Finding relevant themes...")
    progress_bar.progress(25)
    time.sleep(2)  # Simulates processing time

    progress_text.subheader(
        "Found 3 themes in the documents! Please select the one you want to focus on."
    )
    progress_bar.progress(100)  # Ensure the bar runs to the end
    time.sleep(2)  # Give users a moment to see the completion

    # Note the change here: We're now preserving the theme selection on the screen.
    themes = ["Theme 1", "Theme 2", "Theme 3"]  # Mock themes for demonstration
    selected_themes = st.multiselect("Select Relevant Themes:", themes)

    if st.button("Enter", key="process_themes"):
        progress_text.empty()
        progress_bar.empty()
        progress_text.subheader(
            "Searching in database - Rettsdata Neural Network activated."
        )
        progress_bar = st.progress(25)  # Reinitialize progress bar for new task
        time.sleep(2)  # Simulates processing time

        progress_text.subheader("Found historical cases - Rettsdata AI processing.")
        progress_bar.progress(100)
        time.sleep(2)  # Give users a moment to see the completion

        progress_text.empty()
        progress_bar.empty()
        st.success("Process Completed Successfully!")


def main():
    st.set_page_config(layout="wide")
    local_css(
        "/Users/magedhelmy/Desktop/code/playground/OsloHackathonAI2024/streamlit_app/streamlit_app/styles.css"
    )

    st.markdown(
        "<h1 style='text-align: center; font-size: 40px;'>The Next-Generation Lawyer Training Experience</h1>",
        unsafe_allow_html=True,
    )

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    left_col, center_col, right_col = st.columns([1, 2, 1])

    with center_col:
        if not st.session_state["authenticated"]:
            st.image(
                "/Users/magedhelmy/Desktop/code/playground/OsloHackathonAI2024/streamlit_app/streamlit_app/iimage.webp"
            )
            if st.button("Login"):
                st.session_state["authenticated"] = True
                st.experimental_rerun()
        else:
            uploaded_files = st.file_uploader(
                "Choose a file", accept_multiple_files=True
            )

            if uploaded_files:
                if "start_learning_clicked" not in st.session_state:
                    st.session_state["start_learning_clicked"] = False

                # Use an empty placeholder for the button to clear it later
                start_learning_spot = st.empty()

                if not st.session_state["start_learning_clicked"]:
                    if start_learning_spot.button("Start Learning the documents"):
                        st.session_state["start_learning_clicked"] = True
                        start_learning_spot.empty()  # Emptying the spot to remove the button
                        search_and_process_in_database()  # Initiate the theme finding process here without removing the theme selection until "Enter" is pressed


if __name__ == "__main__":
    main()
