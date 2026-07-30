import streamlit as st
import os

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

st.subheader("Visual Troubleshooting Guide Grid")

# Automatically check if the image file exists locally in the repository workspace
image_filename = "dutrex oil.png"
alt_filename = "dutrex_oil.png"

target_file = None
if os.path.exists(image_filename):
    target_file = image_filename
elif os.path.exists(alt_filename):
    target_file = alt_filename

if target_file:
    st.image(target_file, caption="Process Oil Pumping & Troubleshooting Matrix", use_column_width=True)
else:
    # Interactive file uploader fallback if the file isn't found in the root directory yet
    uploaded_file = st.file_uploader("Upload your Troubleshooting Matrix Image (.png or .jpg)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Process Oil Pumping & Troubleshooting Matrix", use_column_width=True)
    else:
        st.warning(f"Please upload your matrix image above or ensure **{image_filename}** is committed directly to your repository folder.")

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
