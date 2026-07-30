import streamlit as st
from PIL import Image

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

st.subheader("Interactive Step-by-Step Troubleshooting Viewer")

# Allow manual upload of the multi-panel picture file
uploaded_file = st.file_uploader("Upload your Troubleshooting Matrix Image (.png or .jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    width, height = img.size

    # Crop the 4 individual panels from the single image grid to display them dynamically like an animated sequence
    # Layout assumed: 2 rows x 3 columns or split quarters
    # Let's crop into 4 distinct troubleshooting quadrants:
    box_cause1 = (0, 0, width // 2, height // 2)
    box_cause2 = (width // 2, 0, width, height // 2)
    box_cause3 = (0, height // 2, width // 3, height)
    box_cause4 = (width // 2, height // 2, width, height)

    # Use radio buttons for smooth, reliable switching without page-refresh blinking
    step = st.radio(
        "Select Troubleshooting Focus Area (Simulated Video Frames):",
        ("Frame 1: Cause 1 & 2 (Viscosity & Nozzle Caking)", 
         "Frame 2: Cause 3 (Air Pockets & Cavitation)", 
         "Frame 3: Cause 4 (Injection Timing & Viscosity)", 
         "Frame 4: Full Summary Matrix View"),
        horizontal=True
    )

    if "Frame 1" in step:
        col_a, col_b = st.columns(2)
        with col_a:
            st.image(img.crop((0, 0, width // 2, height // 2)), caption="Cause 1: Low Oil Temp & Viscosity", use_column_width=True)
        with col_b:
            st.image(img.crop((width // 2, 0, width, height // 2)), caption="Cause 2: Nozzle Blockage (Caking)", use_column_width=True)
        st.success("🔍 **Active Analysis:** Inspecting cold oil thickening and carbon black nozzle buildup.")
        
    elif "Frame 2" in step:
        st.image(img.crop((0, height // 2, width // 2, height)), caption="Cause 3: Air Pockets & Cavitation in Gear Pumps", use_column_width=True)
        st.success("🔍 **Active Analysis:** Checking positive displacement pump line aeration and pressure drops.")
        
    elif "Frame 3" in step:
        st.image(img.crop((width // 2, height // 2, width, height)), caption="Cause 4: Incorrect Injection Timing & Batch Viscosity", use_column_width=True)
        st.success("🔍 **Active Analysis:** Verifying PLC trigger windows against the batch viscosity curve.")
        
    else:
        st.image(img, caption="Complete Troubleshooting & Summary Matrix", use_column_width=True)
        st.success("🔍 **Active Analysis:** Full overview of all operational failure modes and corrective actions.")

else:
    st.warning("Please upload your **dutrex oil.png** image file above to initialize the interactive step viewer.")

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
