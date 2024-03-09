import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import time

def run():
    st.title("AI Training Simulator")

    # Display the AI image. Replace 'image2.jpg' with the path to your AI image
    st.image("image2.jpg", caption="AI Assistant")

    # Simulate an interaction with the AI
    if st.button("Start Practice Session"):
        st.write("Argue for and against your case...")
        simulate_audio_activity()

def simulate_audio_activity():
    # Initializing a placeholder for the chart
    chart_placeholder = st.empty()

    # Base time and audio activity arrays
    time_base = np.linspace(0, 10, num=300)  # Time points
    audio_base = np.abs(np.sin(time_base) * (np.random.rand(len(time_base)) * 0.5 + 0.75)) * 10  # Sine wave modulation

    # Initialize empty DataFrame
    df_audio = pd.DataFrame({"Time": [], "Level": []})

    # Simulating processing time with dynamic updates to simulate audio feedback
    progress_bar = st.progress(0)
    for i in range(1, 11):
        # Update the DataFrame with new "audio level" samples
        new_len = int(len(time_base) * (i / 10))
        df_audio = pd.DataFrame({
            "Time": time_base[:new_len],
            "Level": audio_base[:new_len]
        })

        # Update the chart dynamically
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_audio["Time"], y=df_audio["Level"], fill='tozeroy'))
        fig.update_layout(title="Simulated AI Audio Feedback", xaxis_title="Time", yaxis_title="Level")

        chart_placeholder.plotly_chart(fig, use_container_width=True)

        # Update progress to simulate time passing
        progress_bar.progress(i * 10)
        time.sleep(1)  # Simulate a delay, mimicking real-time feedback

    progress_bar.empty()  # Clear progress bar after completion

    st.success("Practice session completed!")

if __name__ == "__main__":
    run()
