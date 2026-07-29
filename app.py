import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

# Embedded HTML5 Canvas Fluid Animation to simulate oil flow & pump troubleshooting visually on Streamlit Cloud
st.subheader("Visual Process Oil Flow & Injection Animation")
animation_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { margin: 0; background-color: #0e1117; color: white; font-family: sans-serif; text-align: center; }
  canvas { background: #1a1c23; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
</style>
</head>
<body>
<canvas id="oilCanvas" width="700" height="200"></canvas>
<script>
  const canvas = document.getElementById("oilCanvas");
  const ctx = canvas.getContext("2d");
  let particleOffset = 0;

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw Pipeline
    ctx.fillStyle = "#333";
    ctx.fillRect(50, 70, 600, 60);

    // Draw Flow Particles (Oil Injection Simulation)
    ctx.fillStyle = "#ffcc00";
    particleOffset = (particleOffset + 2) % 30;
    for (let x = 60 - particleOffset; x < 640; x += 30) {
      ctx.beginPath();
      ctx.arc(x, 100, 12, 0, Math.PI * 2);
      ctx.fill();
    }

    // Labels
    ctx.fillStyle = "#ffffff";
    ctx.font = "14px sans-serif";
    ctx.fillText("Gear Pump Supply Line", 70, 60);
    ctx.fillText("Banbury Mixing Chamber Injection Nozzle ➔", 380, 155);

    requestAnimationFrame(draw);
  }
  draw();
</script>
</body>
</html>
"""
components.html(animation_html, height=220)

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
