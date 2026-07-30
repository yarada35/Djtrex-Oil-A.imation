import streamlit as st
import os

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

st.subheader("Animated Visual Troubleshooting Guide")

# Automatically detect the static image file to use as the base for the animated layout
image_filename = "dutrex oil.png"
alt_filename = "dutrex_oil.png"

target_image = None
if os.path.exists(image_filename):
    target_image = image_filename
elif os.path.exists(alt_filename):
    target_image = alt_filename

# Inject custom CSS animation so the image gently pulses and loops like a video transition
st.markdown("""
<style>
@keyframes pulseAnimation {
  0% { transform: scale(1); opacity: 0.95; box-shadow: 0 0 0px rgba(0, 150, 255, 0); }
  50% { transform: scale(1.01); opacity: 1; box-shadow: 0 0 15px rgba(0, 150, 255, 0.4); }
  100% { transform: scale(1); opacity: 0.95; box-shadow: 0 0 0px rgba(0, 150, 255, 0); }
}
.animated-container {
  animation: pulseAnimation 4s infinite ease-in-out;
  border-radius: 10px;
  overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

if target_image:
    # Display the image wrapped in the animated container div
    st.markdown('<div class="animated-container">', unsafe_allow_html=True)
    st.image(target_image, use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive timeline progress slider simulating video playback frames
    animation_step = st.slider("Troubleshooting Sequence Timeline (Step-by-Step Animation)", 1, 4, 1)
    
    if animation_step == 1:
        st.caption("▶ **Phase 1 Active:** Examining Cause 1 (Low Oil Temperature & High Viscosity) & Cause 2 (Nozzle Caking).")
    elif animation_step == 2:
        st.caption("▶ **Phase 2 Active:** Inspecting Cause 3 (Air Pockets & Cavitation in Gear Pumps).")
    elif animation_step == 3:
        st.caption("▶ **Phase 3 Active:** Reviewing Cause 4 (Incorrect Injection Timing & Batch Viscosity Curve).")
    else:
        st.caption("▶ **Phase 4 Active:** Summary Checklist & Call to Action.")
else:
    uploaded_file = st.file_uploader("Upload your Troubleshooting Matrix Image (.png or .jpg)", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=True)
    else:
        st.warning(f"Please ensure **{image_filename}** is committed directly to your GitHub repository folder.")

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
