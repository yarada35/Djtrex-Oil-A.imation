import streamlit as st
import os

st.title("Banbury Mixer: Process Oil Troubleshooting Animation")

st.markdown("""
### Troubleshooting Durex / Extender Oil Flow Issues
* **Cause:** Low temperature causes high viscosity and flow stalls.
* **Fix:** Apply trace heating and line heaters to stabilize flow.
""")

if st.button("Generate & Render Animation"):
    with st.spinner("Rendering animation via Manim... Please wait."):
        # Run manim via terminal command from python
        os.system("manim -ql durex_pump_animation.py BanburyTroubleshooting")
        
        # Display the output video if generated successfully
        video_path = "media/videos/durex_pump_animation/480p15/BanburyTroubleshooting.mp4"
        if os.path.exists(video_path):
            st.video(video_path)
        else:
            st.error("Rendering failed due to cloud environment limits. Try running Manim locally on your PC.")
