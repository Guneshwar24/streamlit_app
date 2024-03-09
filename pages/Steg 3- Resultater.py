import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time


def local_css(file_name):
    """Function to incorporate local CSS files into the Streamlit app."""
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def run():
    st.set_page_config(layout="wide")
    local_css("styles_1.css")  # Update with the correct path if needed
    st.title("Grafer - ytelsesvurderinger og historisk data")

    if "analyzed" not in st.session_state:
        # Session state to track if the analysis has been triggered
        st.session_state.analyzed = False

    analyze_button = st.button("Analyser resultater")

    if analyze_button:
        st.session_state.analyzed = True

    if st.session_state.analyzed:
        # Create a function to manage the display sequence with progress
        perform_analysis()


def perform_analysis():
    # Define a list of tuples with the function to call and the message to display
    display_elements_with_messages = [
        (display_radar_chart, "Analyserer generell styrke"),
        (display_historical_performance, "Genererer historisk resultat"),
        (display_comparative_performance, "Genererer komparativ ytelse"),
    ]

    for element, message in display_elements_with_messages:
        # Display the message for the current analysis section
        progress_text = st.subheader(message)

        # Show a progress bar for 5 seconds
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)  # Controls the speed of the progress bar
            progress_bar.progress(percent_complete + 1)

        # Clear the progress bar and text
        progress_bar.empty()
        progress_text.empty()

        # Display the current element (chart or table)
        element()


def display_radar_chart():
    categories = [
        "Tone",
        "Klarhet",
        "selvtillit",
        "Har tatt tak i alle svakhetene",
        "Har tatt tak i alle styrkene",
    ]
    # Sample ratings for after training
    ratings_after = [4, 4.5, 4.2, 3.8, 4.7]
    # Introducing ratings for before training, as an example
    ratings_before = [3, 3.5, 3.2, 2.8, 3.7]

    # Radar chart for before training
    fig_radar = go.Figure()
    fig_radar.add_trace(
        go.Scatterpolar(
            r=ratings_before,
            theta=categories,
            fill="toself",
            name="F⌀r Trening",
            marker_color="red",
        )
    )

    # Radar chart for after training
    fig_radar.add_trace(
        go.Scatterpolar(
            r=ratings_after,
            theta=categories,
            fill="toself",
            name="Etter Trening",
            marker_color="blue",
        )
    )

    # Update layout for a cohesive look
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=True
    )

    st.plotly_chart(fig_radar, use_container_width=True)


def display_historical_performance():
    st.subheader("Historisk ytelsesforbedring")
    performance_scores = [70, 80, 95, 90, 95]

    df_history = pd.DataFrame(
        {
            "Måneder": ["Runde 1", "Runde 2", "Runde 3", "Runde 4", "Runde 5"],
            "Ytelse": performance_scores,
        }
    )

    fig_history = px.line(
        df_history,
        x="Måneder",
        y="Ytelse",
        markers=True,
        title="Ytelse Over Tid",
    )
    fig_history.update_traces(line=dict(width=3))
    fig_history.update_layout(
        plot_bgcolor="white",
        xaxis=dict(showline=True, showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="lightgray"),
    )

    st.plotly_chart(fig_history, use_container_width=True)


def display_comparative_performance():
    st.subheader("Komparativ ytelse")

    data = {
        "Metric": ["N⌀yaktighet", "Hastighet", "Konsistens"],
        "Din Score": [75, 80, 85],
        "Gjennomsnittlig Kollega score": [60, 55, 53],
    }
    df_comparison = pd.DataFrame(data)

    st.table(
        df_comparison.style.format(
            subset=["Din Score", "Gjennomsnittlig Kollega score"], formatter="{:.2f}"
        )
        .bar(
            subset=["Din Score"], color="#5fba7d", width=100
        )  # Full width for green bars
        .bar(
            subset=["Gjennomsnittlig Kollega score"], color="#FFA07A", width=50
        )  # Reduced width for orange bars
    )


if __name__ == "__main__":
    run()
