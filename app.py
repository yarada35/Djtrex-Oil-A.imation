import streamlit as st
from PIL import Image

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

st.subheader("Interactive Engineering Troubleshooting Sequences")

# Allow manual upload of the comprehensive matrix image file
uploaded_file = st.file_uploader("Upload your Troubleshooting Matrix Image (.png or .jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    width, height = img.size

    # Precise crop boxes matching the exact 2x3 panel layout of your image grid:
    # Top Row: Cause 1 (Left half of top), Cause 2 (Right half of top)
    # Bottom Row: Cause 3 (Left third), Conclusion (Middle third), Cause 4 (Right third)
    box_c1 = (0, 0, width // 2, height // 2)
    box_c2 = (width // 2, 0, width, height // 2)
    box_c3 = (0, height // 2, width // 3, height)
    box_conclusion = (width // 3, height // 2, 2 * (width // 3), height)
    box_c4 = (2 * (width // 3), height // 2, width, height)

    # Professional selection tabs mapped directly to your technical scenarios
    scene_option = st.radio(
        "Select Troubleshooting Scene Sequence:",
        (
            "Scene 2: Cause 1 — Low Oil Temp & High Viscosity",
            "Scene 3: Cause 2 — Nozzle Blockage (Caking)",
            "Scene 4: Cause 3 — Air Pockets & Cavitation",
            "Scene 5: Cause 4 — Incorrect Injection Timing",
            "Scene 6: Conclusion / Full Matrix Overview"
        ),
        horizontal=False
    )

    if "Scene 2" in scene_option:
        st.image(img.crop(box_c1), use_column_width=True)
        st.markdown("### Scene 2: Cause 1 — Low Oil Temperature & High Viscosity")
        st.write("**Visual:** A macro-photographic close-up of the pipeline. An industrial-grade bimetallic thermometer probe reads 15°C. Process oil appears dark, cloudy, and sluggish in thick gelatinous clumps.")
        st.success("**Solution Visual:** Trace heating toggle switches to 'ON'. A shimmering heat haze ripples around the pipe, instantly turning the oil clear, amber, and fast-flowing.")
        st.info("**On-Screen Text:**\n* **Cause:** Low Temp / High Viscosity\n* **Fix:** Check Line Heaters & Trace Heating")

    elif "Scene 3" in scene_option:
        st.image(img.crop(box_c2), use_column_width=True)
        st.markdown("### Scene 3: Cause 2 — Nozzle Blockage (Caking)")
        st.write("**Visual:** Close-up inside the open throat of the Banbury mixing chamber. The nozzle port is completely encased in a hard, black, carbonized crust of baked rubber and soot.")
        st.success("**Solution Visual:** A maintenance dry-ice blaster tool targets the tip, rapidly blasting away the black crust to reveal a clean, wide-open spray port.")
        st.info("**On-Screen Text:**\n* **Cause:** Premature Absorption & Nozzle Caking\n* **Fix:** Inspect, Purge, and Clean Nozzles")

    elif "Scene 4" in scene_option:
        st.image(img.crop(box_c3), use_column_width=True)
        st.markdown("### Scene 4: Cause 3 — Air Pockets & Cavitation")
        st.write("**Visual:** Industrial cutaway of the process oil gear pump. Large air bubbles are trapped between meshing gear teeth, causing stuttering delivery. Discharge pressure gauge wildly swings between 2 bar and 10 bar.")
        st.success("**Solution Visual:** Bleed valve turns green and purges trapped air/oil spray. Pressure gauge locks dead-center at 7 bar in the green zone, and gear pump spins smoothly.")
        st.info("**On-Screen Text:**\n* **Cause:** Air Pockets & Cavitation\n* **Fix:** Bleed Supply Lines & Restore Pressure")

    elif "Scene 5" in scene_option:
        st.image(img.crop(box_c4), use_column_width=True)
        st.markdown("### Scene 5: Cause 4 — Incorrect Injection Timing")
        st.write("**Visual:** Internal view of counter-rotating Banbury rotors shearing solid polymer. Oil injected too early sits as an idle pool, causing batch viscosity curve to slump sharply.")
        st.success("**Solution Visual:** PLC timeline shifts oil injection two phases later during high-shear phase. Oil sprays as a fine mist, and torque curve stabilizes into a smooth operational waveform.")
        st.info("**On-Screen Text:**\n* **Cause:** Incorrect Injection Timing\n* **Fix:** Verify PLC Sequence & Injection Point")

    else:
        col_left, col_right = st.columns(2)
        with col_left:
            st.image(img.crop(box_conclusion), use_column_width=True)
        with col_right:
            st.image(img, use_column_width=True)
        st.markdown("### Scene 6: Conclusion / Call to Action")
        st.write("**Visual:** Split-screen industrial view showing rapid oil flow, clean mixing chambers, and stable waveform monitoring.")
        st.success("**Summary Checklist:**\n1. Verify Temp/Viscosity\n2. Inspect & Purge Nozzles\n3. Bleed Lines\n4. Check PLC Timing")

else:
    st.warning("Please upload your **dutrex oil.png** image file above to activate the scene-by-scene troubleshooting player.")

# Static Engineering Reference Sections Below
st.markdown("---")
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
