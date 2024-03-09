import streamlit as st
import time


def local_css(file_name):
    """Function to incorporate local CSS files into the Streamlit app."""
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def search_and_process_in_database():
    """Simulerer prosessen med å søke og velge temaer fra en database."""
    progress_text = st.empty()
    progress_bar = st.progress(0)

    progress_text.subheader("Å finne relevante temaer...")
    progress_bar.progress(25)
    time.sleep(2)  # Simulates the time taken to find themes

    progress_text.subheader(
        "Fant 3 temaer i dokumentene! Vennligst velg det du vil fokusere på."
    )
    progress_bar.progress(100)
    time.sleep(2)  # Simulated delay

    # Available themes
    themes = ["Eiendomsrett", "Menneskerett", "Prosessrett"]

    # Display the themes in Streamlit
    st.write("### Tilgjengelige temae:")
    for i, theme in enumerate(themes, start=1):
        st.write(f"{i}. {theme}")
    time.sleep(2)  # Simulated delay

    process_selected_theme()


def process_selected_theme():
    """Håndterer etterbehandlingen av temaseleksjonen."""
    with st.spinner("Behandling pågår... Vennligst vent"):
        progress_text = st.empty()
        progress_bar = st.progress(25)
        progress_text.subheader("Søker i database - Nevralnett aktivert.")
        time.sleep(2)

        progress_bar.progress(50)
        progress_text.subheader("Fant historiske tilfeller - AI-behandling pågår.")
        time.sleep(2)
        progress_bar.progress(100)

        time.sleep(1)  # Simulate finalization process.
        progress_text.empty()
        progress_bar.empty()
        st.success("Prosess fullført vellykket!")


def main():

    st.set_page_config(layout="wide", page_title="Hovedside")
    local_css("styles.css")  # Update with the correct path if needed

    st.markdown(
        "<h1 style='text-align: center; font-size: 40px;'> LegalPredictors Simulator</h1>",
        unsafe_allow_html=True,
    )

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    left_col, center_col, right_col = st.columns([1, 2, 1])

    with center_col:
        if not st.session_state["authenticated"]:
            st.image("image.webp")  # Update with the correct path if needed
            if st.button("Logg inn"):
                st.session_state["authenticated"] = True
                st.experimental_rerun()
        else:
            uploaded_files = st.file_uploader("Velg en fil", accept_multiple_files=True)

            if uploaded_files:
                start_learning_spot = st.empty()

                if not st.session_state.get("start_learning_clicked"):
                    if start_learning_spot.button("Begynn å lære dokumentene"):
                        st.session_state["start_learning_clicked"] = True
                        start_learning_spot.empty()
                        search_and_process_in_database()
                        # process_selected_theme is now called within search_and_process_in_database if a theme is selected


if __name__ == "__main__":
    main()
