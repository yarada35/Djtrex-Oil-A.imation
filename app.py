import streamlit as st
import time

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

st.subheader("Animated Troubleshooting Guide Player")

# Allow manual upload of the picture file
uploaded_file = st.file_uploader("Upload your Troubleshooting Matrix Image (.png or .jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Interactive playback controls simulating a video player
    col1, col2, col3 = st.columns([1, 1, 2])
    play_animation = col1.button("▶ Play Animation")
    pause_animation = col2.button("⏸ Pause")
    
    # Session state for frame-by-frame animation simulation
    if 'frame' not in st.session_state:
        st.session_state.frame = 1

    if play_animation:
        for i in range(1, 5):
            st.session_state.frame = i
            time.sleep(1.5)
            st.rerun()

    # Display the image with dynamic visual highlights based on the active troubleshooting step
    st.image(uploaded_file, caption=f"Active Playback Frame: Step {st.session_state.frame} of 4", use_column_width=True)
    
    # Step descriptions matching the video frames
    if st.session_state.frame == 1:
        st.success("🎥 **Playing [0:00 - 0:15]:** Cause 1 (Low Oil Temp & High Viscosity) & Cause 2 (Nozzle Caking).")
    elif st.session_state.frame == 2:
        st.success("🎥 **Playing [0:15 - 0:30]:** Cause 3 (Air Pockets & Cavitation in Gear Pumps).")
    elif st.session_state.frame == 3:
        st.success("🎥 **Playing [0:30 - 0:45]:** Cause 4 (Incorrect Injection Timing & Viscosity Curve).")
    else:
        st.success("🎥 **Playing [0:45 - 1:00]:** Conclusion & Summary Checklist.")
else:
    st.warning("Please upload your **dutrex oil.png** image above to start the interactive visual player.")

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
