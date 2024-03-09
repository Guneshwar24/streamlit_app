import streamlit as st
from streamlit_echarts import st_echarts
import time


def local_css(file_name):
    """Function to incorporate local CSS files into the Streamlit app."""
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def run():
    st.set_page_config(layout="wide")
    local_css("styles_1.css")  # Update with the correct path if needed
    st.title("Styrker og svakheter i saken")

    if "analysis_stage" not in st.session_state:
        st.session_state.analysis_stage = 0

    if st.button("Analyser dokumentet"):
        st.session_state.analysis_stage = 1

    # Arguments in favor
    if st.session_state.analysis_stage == 1:
        progress_time()
        display_arguments_table(in_favor=True)
        st.session_state.analysis_stage = 2

    # Arguments against
    if st.session_state.analysis_stage == 2:
        progress_time()
        display_arguments_table(in_favor=False)
        st.session_state.analysis_stage = 3

    # Speedometer display at the end
    if st.session_state.analysis_stage == 3:
        progress_time()
        display_speedometer()
        st.session_state.analysis_stage = (
            0  # Reset or leave as is to stop further executions
        )
        if st.button("Start Simulator"):
            with st.spinner("Processing... Please wait"):
                progress_text = st.empty()
                progress_bar = st.progress(25)
                progress_text.subheader("Starting Rettsdata AI")
                time.sleep(4)

                progress_bar.progress(50)
                progress_text.subheader("Starting Simulator")
                time.sleep(3)
                progress_bar.progress(100)

                st.success("Ready!")


def display_arguments_table(in_favor=True):
    """Displays the arguments table with styles."""
    if in_favor:
        html_content = """
        ### Argumenter som taler for: 
        <span style='color: green;'>1. **Bruker jordbrukshensyn som et relevant hensyn:** *Rt-2004-1092* (1974), LA-2005-1939.</span><br>
        <span style='color: green;'>2. **Legger vekt på at lovens byggeforbud var tidsbegrenset:** Rt-1970-67, *LA-2003-1221*, *LG-1999-2121*.</span><br>
        <span style='color: green;'>3. **Legger vekt på gårdens behov:** 1982-1541 *LH-2001-323*, *LG-2004-544* (1967).</span><br>
        """
    else:
        html_content = """
        ### Argumenter som taler mot:
        <span style='color: red;'>1. **Manglende balanse mellom jordbrukshensyn og andre samfunnsinteresser:** *Rt-2012-1836* (1963).</span><br>
        <span style='color: red;'>2. **Manglende tilpasning til endrede omstendigheter:** *Rt-2017-1349 (2017)* (2017).</span><br>
        <span style='color: red;'>3. **Utilstrekkelig hensyn til miljømessige og bærekraftige hensyn:** *Rt-2018-277 (2018)*.</span><br>
        """

    st.markdown(html_content, unsafe_allow_html=True)


def progress_time():
    """Shows a progress bar with a message for a brief moment."""
    # Create a placeholder for the message
    message = st.empty()
    message.text("Argumenter med KI...")  # Display the message

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)  # Adjust the time to control the speed of the progress bar
        progress.progress(i + 1)

    progress.empty()  # This removes the progress bar
    message.empty()  # Also remove the message after completion


def display_speedometer():
    """Displays a speedometer gauge using ECharts"""
    option = {
        "series": [
            {
                "type": "gauge",
                "startAngle": 180,
                "endAngle": 0,
                "min": 0,
                "max": 100,
                "splitNumber": 4,
                "axisLine": {
                    "lineStyle": {
                        "width": 6,
                        "color": [
                            [0.25, "#FF6E76"],
                            [0.5, "#FDDD60"],
                            [0.75, "#58D9F9"],
                            [1, "#7CFFB2"],
                        ],
                    },
                },
                "pointer": {"width": 5},
                "axisTick": {
                    "distance": -30,
                    "length": 8,
                    "lineStyle": {"color": "#FFF", "width": 2},
                },
                "splitLine": {
                    "distance": -40,
                    "length": 30,
                    "lineStyle": {"color": "#FFF", "width": 4},
                },
                "axisLabel": {"color": "auto", "distance": 40, "fontSize": 15},
                "detail": {
                    "valueAnimation": True,
                    "formatter": "Sannsynligheten for  ",
                    "color": "auto",
                },
                "data": [{"value": 75}],
            }
        ]
    }
    st_echarts(option, height="500px")


if __name__ == "__main__":
    run()
