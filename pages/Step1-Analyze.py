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
    st.title("Strength and Weaknesses of the Case")

    if "analysis_stage" not in st.session_state:
        st.session_state.analysis_stage = 0

    if st.button("Analyze Document"):
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
        ### Arguments in Favor of the Merger: 
        <span style='color: green;'>1. **Promotes Economic Efficiency:** *United States v. General Dynamics Corp.* (1974), *FTC v. Procter & Gamble Co.* (1967).</span><br>
        <span style='color: green;'>2. **Lack of Substantial Market Overlap:** *United States v. Marine Bancorporation, Inc.* (1974), *United States v. Baker Hughes Inc.* (1990).</span><br>
        <span style='color: green;'>3. **Necessary for Competitive Survival:** *United States v. Citizens & Southern National Bank* (1975), *United States v. First City National Bank of Houston* (1967).</span><br>
        """
    else:
        html_content = """
        ### Arguments Against the Merger:
        <span style='color: red;'>1. **Reduces Market Competition:** *United States v. Philadelphia National Bank* (1963), *United States v. Alcoa* (1964).</span><br>
        <span style='color: red;'>2. **Harmful to Consumers:** *United States v. AT&T Inc.* (2018), *United States v. Aetna Inc.* (2017).</span><br>
        <span style='color: red;'>3. **Violates Antitrust Principles:** *Standard Oil Co. of New Jersey v. United States* (1911), *United States v. Microsoft Corp.* (2001).</span><br>
        """

    st.markdown(html_content, unsafe_allow_html=True)


def progress_time():
    """Shows a progress bar with a message for a brief moment."""
    # Create a placeholder for the message
    message = st.empty()
    message.text("Analyzing with AI...")  # Display the message

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
                    "formatter": "Highly Likely to win the case ",
                    "color": "auto",
                },
                "data": [{"value": 75}],
            }
        ]
    }
    st_echarts(option, height="500px")


if __name__ == "__main__":
    run()
