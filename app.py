import streamlit as st
import base64
import os

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

st.subheader("Visual Troubleshooting Guide Grid")

# Option A: If banbury_grid.png is uploaded in the repository folder, display it directly.
# Option B: If you want to embed the grid image inline via base64, place your base64 string below.
image_filename = "banbury_grid.png"

if os.path.exists(image_filename):
    st.image(image_filename, caption="Process Oil Pumping & Troubleshooting Matrix", use_column_width=True)
else:
    # Embedded Base64 representation of the 6-panel grid image to render instantly without external file uploads
    grid_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    
    # If you save your generated grid image bytes, you can also render it via HTML/Base64 like this:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="data:image/png;base64,{grid_base64}" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);" alt="Troubleshooting Grid">
    </div>
    <div style="padding: 15px; background-color: #1a1c23; border-radius: 8px; border: 1px solid #4f4f5f; text-align: center;">
        <p style="color: #ffcc00; font-size: 13px; margin: 0;"><b>Tip:</b> To display your full high-res multi-panel image, save it as <b>banbury_grid.png</b> in your GitHub repository folder.</p>
    </div>
    """, unsafe_allow_html=True)

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
