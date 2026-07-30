import streamlit as st
from PIL import Image

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Interactive Real-Life Simulation Dashboard")

st.info("Select a troubleshooting sequence below to trigger live-action simulation movements, fluid dynamics, and operational fixes.")

# File uploader for the source matrix image
uploaded_file = st.file_uploader("Upload your Troubleshooting Matrix Image (.png or .jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    width, height = img.size

    # Crop coordinates mapping the panels
    box_c1 = (0, 0, width // 2, height // 2)
    box_c2 = (width // 2, 0, width, height // 2)
    box_c3 = (0, height // 2, width // 3, height)
    box_conclusion = (width // 3, height // 2, 2 * (width // 3), height)
    box_c4 = (2 * (width // 3), height // 2, width, height)

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
        st.write("**Live Simulation:** Real-time fluid flow monitoring showing thick, sluggish oil clumping at 15°C.")
        
        # Interactive HTML5/CSS animated fluid state / heat haze simulation
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 20px; border-radius: 12px; color: #fff; border: 1px solid #334155;">
            <h4 style="color: #38bdf8; margin-top:0;">Live Thermal & Fluid Dynamics Engine</h4>
            <p><b>Status:</b> <span id="heat-status" style="color: #f43f5e; font-weight: bold;">TRACE HEATING OFF (Sluggish Flow)</span></p>
            <div style="width: 100%; height: 24px; background: #334155; border-radius: 12px; overflow: hidden; position: relative;">
                <div id="fluid-bar" style="width: 30%; height: 100%; background: #f43f5e; transition: width 0.8s ease, background 0.8s ease;"></div>
            </div>
            <br>
            <button onclick="
                document.getElementById('fluid-bar').style.width = '100%';
                document.getElementById('fluid-bar').style.background = '#10b981';
                document.getElementById('heat-status').innerHTML = 'TRACE HEATING ON (Fast Amber Flow Active)';
                document.getElementById('heat-status').style.color = '#10b981';
            " style="background: #0284c7; color: white; border: none; padding: 10px 18px; border-radius: 6px; cursor: pointer; font-weight: bold;">Toggle Trace Heating ON</button>
        </div>
        """, unsafe_allow_html=True)

        st.success("**Solution Visual:** Trace heating toggle switches to 'ON'. Shimmering heat haze ripples around the pipe, transforming oil into a fast, amber stream.")
        st.info("**On-Screen Text:**\n* **Cause:** Low Temp / High Viscosity\n* **Fix:** Check Line Heaters & Trace Heating")

    elif "Scene 3" in scene_option:
        st.image(img.crop(box_c2), use_column_width=True)
        st.markdown("### Scene 3: Cause 2 — Nozzle Blockage (Caking)")
        st.write("**Live Simulation:** Inspection of the Banbury mixing chamber throat showing severe carbonized crust buildup sealing the port.")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 20px; border-radius: 12px; color: #fff; border: 1px solid #334155;">
            <h4 style="color: #38bdf8; margin-top:0;">Dry-Ice Blaster Cleaning Simulation</h4>
            <p><b>Nozzle State:</b> <span id="nozzle-status" style="color: #f43f5e; font-weight: bold;">BLOCKED (Carbon Caked)</span></p>
            <button onclick="
                document.getElementById('nozzle-status').innerHTML = 'CLEANED & PURGED (Wide-Open Spray Port)';
                document.getElementById('nozzle-status').style.color = '#10b981';
            " style="background: #059669; color: white; border: none; padding: 10px 18px; border-radius: 6px; cursor: pointer; font-weight: bold;">Trigger Dry-Ice Blaster</button>
        </div>
        """, unsafe_allow_html=True)

        st.success("**Solution Visual:** Maintenance tool dry-ice blaster targets the nozzle tip, rapidly stripping away black carbon buildup.")
        st.info("**On-Screen Text:**\n* **Cause:** Premature Absorption & Nozzle Caking\n* **Fix:** Inspect, Purge, and Clean Nozzles")

    elif "Scene 4" in scene_option:
        st.image(img.crop(box_c3), use_column_width=True)
        st.markdown("### Scene 4: Cause 3 — Air Pockets & Cavitation")
        st.write("**Live Simulation:** Real-life gear pump internal cutaway with trapped air pockets causing mechanical stutter and pressure surges (2 bar to 10 bar). Includes live audio-visual simulation placeholder.")

        # HTML5 Audio Web Audio API generator for live cavitation sound effect
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 20px; border-radius: 12px; color: #fff; border: 1px solid #334155;">
            <h4 style="color: #38bdf8; margin-top:0;">Live Cavitation Audio & Pressure Rig</h4>
            <p><b>Pressure Gauge:</b> <span id="pressure-val" style="color: #f43f5e; font-weight: bold;">ERRATIC (2 - 10 bar fluctuating)</span></p>
            <button onclick="
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(120, ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(40, ctx.currentTime + 0.5);
                gain.gain.setValueAtTime(0.3, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.5);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 0.5);
                document.getElementById('pressure-val').innerHTML = 'STABLE (Locked at 7 bar Green Zone)';
                document.getElementById('pressure-val').style.color = '#10b981';
            " style="background: #d97706; color: white; border: none; padding: 10px 18px; border-radius: 6px; cursor: pointer; font-weight: bold;">🔊 Simulate Bleed & Cavitation Sound</button>
        </div>
        """, unsafe_allow_html=True)

        st.success("**Solution Visual:** Purge valve opens, ejecting trapped air. Pressure gauge locks dead-center at 7 bar in the green zone.")
        st.info("**On-Screen Text:**\n* **Cause:** Air Pockets & Cavitation\n* **Fix:** Bleed Supply Lines & Restore Pressure")

    elif "Scene 5" in scene_option:
        st.image(img.crop(box_c4), use_column_width=True)
        st.markdown("### Scene 5: Cause 4 — Incorrect Injection Timing")
        st.write("**Live Simulation:** Banbury mixer internal rotor shearing sequence with live viscosity curve monitoring.")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 20px; border-radius: 12px; color: #fff; border: 1px solid #334155;">
            <h4 style="color: #38bdf8; margin-top:0;">PLC Sequential Injection Synchronizer</h4>
            <p><b>Viscosity Waveform:</b> <span id="plc-status" style="color: #f43f5e; font-weight: bold;">SLUMPED (Incorrect Timing)</span></p>
            <button onclick="
                document.getElementById('plc-status').innerHTML = 'STABILIZED (Optimized High-Shear Mist Injection)';
                document.getElementById('plc-status').style.color = '#10b981';
            " style="background: #7c3aed; color: white; border: none; padding: 10px 18px; border-radius: 6px; cursor: pointer; font-weight: bold;">Shift PLC Timing Sequence</button>
        </div>
        """, unsafe_allow_html=True)

        st.success("**Solution Visual:** PLC timeline shifts oil injection two phases later. Oil sprays as a fine mist during high-shear, stabilizing torque waveform.")
        st.info("**On-Screen Text:**\n* **Cause:** Incorrect Injection Timing\n* **Fix:** Verify PLC Sequence & Injection Point")

    else:
        col_left, col_right = st.columns(2)
        with col_left:
            st.image(img.crop(box_conclusion), use_column_width=True)
        with col_right:
            st.image(img, use_column_width=True)
        st.markdown("### Scene 6: Conclusion / Call to Action")
        st.write("**Live Simulation:** Full matrix synchronized overview combining all operational corrective actions.")
        st.success("**Summary Checklist:**\n1. Verify Temp/Viscosity\n2. Inspect & Purge Nozzles\n3. Bleed Lines\n4. Check PLC Timing")

else:
    st.warning("Please upload your **dutrex oil.png** image file above to activate the live interactive simulation player.")

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
