import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time


def run():
    st.title("Modern Looking Graphs - Performance Ratings and Historical Data")

    if "analyzed" not in st.session_state:
        # Session state to track if the analysis has been triggered
        st.session_state.analyzed = False

    analyze_button = st.button("Analyze Results")

    if analyze_button:
        st.session_state.analyzed = True

    if st.session_state.analyzed:
        # Create a function to manage the display sequence with progress
        perform_analysis()


def perform_analysis():
    # Define a list of tuples with the function to call and the message to display
    display_elements_with_messages = [
        (display_radar_chart, "Creating overall strength"),
        (display_historical_performance, "Generating historical performance"),
        (display_comparative_performance, "Generating comparative performance"),
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
        "Clarity",
        "Confidence",
        "Addressed all weaknesses",
        "Covered all strengths",
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
            name="Before Training",
            marker_color="red",
        )
    )

    # Radar chart for after training
    fig_radar.add_trace(
        go.Scatterpolar(
            r=ratings_after,
            theta=categories,
            fill="toself",
            name="After Training",
            marker_color="blue",
        )
    )

    # Update layout for a cohesive look
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=True
    )

    st.plotly_chart(fig_radar, use_container_width=True)


def display_historical_performance():
    st.subheader("Historical Performance Improvement")
    performance_scores = [70, 80, 95, 90, 95]

    df_history = pd.DataFrame(
        {
            "Month": ["Round 1", "Round 2", "Round 3", "Round 4", "Round 5"],
            "Performance": performance_scores,
        }
    )

    fig_history = px.line(
        df_history,
        x="Month",
        y="Performance",
        markers=True,
        title="Performance Over Time",
    )
    fig_history.update_traces(line=dict(width=3))
    fig_history.update_layout(
        plot_bgcolor="white",
        xaxis=dict(showline=True, showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="lightgray"),
    )

    st.plotly_chart(fig_history, use_container_width=True)


def display_comparative_performance():
    st.subheader("Comparative Performance")

    data = {
        "Metric": ["Accuracy", "Speed", "Consistency"],
        "Your Score": [75, 80, 85],
        "Average Peer Score": [60, 55, 53],
    }
    df_comparison = pd.DataFrame(data)

    st.table(
        df_comparison.style.format(
            subset=["Your Score", "Average Peer Score"], formatter="{:.2f}"
        )
        .bar(
            subset=["Your Score"], color="#5fba7d", width=100
        )  # Full width for green bars
        .bar(
            subset=["Average Peer Score"], color="#FFA07A", width=50
        )  # Reduced width for orange bars
    )


if __name__ == "__main__":
    run()
