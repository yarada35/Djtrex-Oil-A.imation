import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Banbury Mixer Troubleshooting", layout="centered")

st.title("🏭 Banbury Mixer: Process Oil Pumping Guide")
st.markdown("### Troubleshooting Durex / Extender Oil Flow Issues")

st.info("This dashboard outlines common flow restrictions, root causes, and corrective actions for rubber process oil injection systems.")

# Enhanced Multi-Element Industrial Animation Component (Gear Pump + Flow + Nozzle Injection)
st.subheader("Visual Process Oil Flow & Injection Animation")
animation_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { margin: 0; background-color: #0e1117; color: white; font-family: sans-serif; text-align: center; display: flex; justify-content: center; align-items: center; height: 210px; }
  canvas { background: #1a1c23; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
</style>
</head>
<body>
<canvas id="oilCanvas" width="700" height="190"></canvas>
<script>
  const canvas = document.getElementById("oilCanvas");
  const ctx = canvas.getContext("2d");
  let angle = 0;
  let particleOffset = 0;

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 1. Draw Gear Pump Housing (Left side)
    ctx.fillStyle = "#262730";
    ctx.fillRect(30, 55, 90, 80);
    ctx.strokeStyle = "#4f4f5f";
    ctx.lineWidth = 3;
    ctx.strokeRect(30, 55, 90, 80);

    // Rotating Gear Teeth Indicator (Left)
    ctx.save();
    ctx.translate(75, 95);
    ctx.rotate(angle);
    ctx.fillStyle = "#ffcc00";
    for (let i = 0; i < 6; i++) {
      ctx.rotate(Math.PI / 3);
      ctx.fillRect(-6, -22, 12, 8);
    }
    ctx.beginPath();
    ctx.arc(0, 0, 10, 0, Math.PI * 2);
    ctx.fillStyle = "#0e1117";
    ctx.fill();
    ctx.restore();

    // 2. Draw Pipeline
    ctx.fillStyle = "#262730";
    ctx.fillRect(120, 75, 480, 40);

    // 3. Draw Moving Oil Flow Particles inside Pipeline
    ctx.fillStyle = "#ffcc00";
    particleOffset = (particleOffset + 3) % 30;
    for (let x = 130 - particleOffset; x < 590; x += 30) {
      ctx.beginPath();
      ctx.arc(x, 95, 8, 0, Math.PI * 2);
      ctx.fill();
    }

    // 4. Draw Banbury Chamber Injection Nozzle (Right side)
    ctx.fillStyle = "#3b3c4f";
    ctx.fillRect(600, 45, 70, 100);
    ctx.fillStyle = "#ff4b4b";
    ctx.fillRect(610, 80, 20, 30); // Spray zone

    // 5. Labels & Text Indicators
    ctx.fillStyle = "#ffffff";
    ctx.font = "12px sans-serif";
    ctx.fillText("Gear Pump", 45, 45);
    ctx.fillText("Supply Line ➔", 280, 65);
    ctx.fillText("Mixing Chamber Nozzle", 560, 165);

    angle += 0.05;
    requestAnimationFrame(draw);
  }
  draw();
</script>
</body>
</html>
"""
components.html(animation_html, height=210)

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
