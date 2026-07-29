import streamlit as st
import os

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

# Displaying the comprehensive industrial troubleshooting visual overview grid
st.subheader("Visual Troubleshooting Guide Grid")

# If you prefer to embed the image directly via base64 so you don't even need to upload a separate file to GitHub, 
# you can use an HTML wrapper, or keep checking for 'banbury_grid.png'. 
image_filename = "banbury_grid.png"

if os.path.exists(image_filename):
    st.image(image_filename, caption="Process Oil Pumping & Troubleshooting Matrix", use_column_width=True)
else:
    # Fallback option: displays a helpful instruction or you can place your image bytes directly.
    st.markdown("""
    <div style="padding: 20px; background-color: #1e1e2f; border-radius: 10px; border: 1px solid #4f4f5f; text-align: center;">
        <p style="color: #ffcc00; font-weight: bold; margin-bottom: 10px;">📌 Action Required for GitHub Deployment:</p>
        <p style="color: #ffffff; font-size: 14px;">Please save your generated 6-panel troubleshooting overview image as <b>banbury_grid.png</b> and commit it directly to your GitHub repository root folder.</p>
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
