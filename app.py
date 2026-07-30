import streamlit as st
import os

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

st.subheader("Visual Troubleshooting Guide Video")

# Check for video file variants in the GitHub repository working directory
video_filename = "dutrex oil.mp4"
alt_filename = "dutrex_oil.mp4"

target_video = None
if os.path.exists(video_filename):
    target_video = video_filename
elif os.path.exists(alt_filename):
    target_video = alt_filename

if target_video:
    st.video(target_video)
else:
    # Interactive video uploader fallback if the video isn't committed in the root directory yet
    uploaded_video = st.file_uploader("Upload your Troubleshooting Matrix Video (.mp4)", type=["mp4", "mov", "avi"])
    
    if uploaded_video is not None:
        st.video(uploaded_video)
    else:
        st.warning(f"Please upload your matrix video above or ensure **{video_filename}** is committed directly to your GitHub repository folder.")

# Troubleshooting Sections
st.subheader("1. Low Oil Temperature / High Viscosity")
st.write("**Cause:** Process oil becomes too thick if ambient or line temperatures drop, preventing smooth pumping.")
st.success("**Fix:** Check line heaters and trace heating to maintain target fluid temperatures.")

st.subheader("2. Premature Absorption or Blockage")
st.write("**Cause:** Injection nozzles positioned too close to hot mixing zones cause rubber-oil caking and carbon black buildup.")
st.success("**Fix:** Purge and clean the injection port regularly.")

st.subheader("3. Air Pockets or Cavitation")
st.write("**Cause:** Trapped air or foaming in the supply lines creates erratic positive displacement or gear pump delivery.")
st.success("**Fix:** Bleed supply lines to remove trapped air pockets and restore uniform pressure.")

st.subheader("4. Incorrect Injection Timing")
st.write("**Cause:** Oil injected too early or late in the mixing cycle abruptly alters batch viscosity.")
st.success("**Fix:** Verify PLC sequence triggers oil injection only after proper initial breakdown of polymers and fillers.")
