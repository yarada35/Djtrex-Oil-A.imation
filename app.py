import streamlit as st

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

st.subheader("Visual Troubleshooting Guide Grid")

# Displaying the image directly using a standard markdown/HTML image tag referencing an accessible public image URL or direct base64
image_url = "https://i.ibb.co/3s7N9r3/watermarked-img-378759811578840393.png"

st.markdown(f"""
<div style="text-align: center; margin-bottom: 20px;">
    <img src="{image_url}" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);" alt="Troubleshooting Grid">
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
