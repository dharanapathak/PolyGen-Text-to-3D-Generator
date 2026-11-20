import streamlit as st
import plotly.graph_objects as go
from src.prompt_processor import process_prompt
from src.primitive_generator import build_asset

st.set_page_config(page_title="PolyGen | Group 8", page_icon="🧊", layout="wide")
st.title("🧊 PolyGen — Text-to-3D Asset Pipeline")
st.caption("Internship prototype • Group 8 • Infotact Solutions")
st.info("Week 2 prototype: prompt processing + procedural primitive preview/export. This is not yet an AI text-to-3D model integration.")

prompt = st.text_area("Describe a 3D object", placeholder="e.g., a blue futuristic car", height=110)
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Prototype supports:** cube, sphere, cylinder, cone, robot (multi-part primitives).")
with col2:
    st.markdown("**Next development:** connect a text-to-3D model/API in Weeks 3–4.")
if st.button("Generate prototype asset", type="primary", disabled=not prompt.strip()):
    parsed = process_prompt(prompt)
    meshes = build_asset(parsed)
    st.subheader("Prompt analysis")
    st.write(f"Detected asset type: **{parsed['shape']}**")
    st.write(f"Detected color keyword: **{parsed['color']}**")
    st.write(f"Processed description: {parsed['description']}")
    fig = go.Figure()
    for mesh in meshes:
        fig.add_trace(go.Mesh3d(x=mesh['x'], y=mesh['y'], z=mesh['z'], i=mesh['i'], j=mesh['j'], k=mesh['k'], color=parsed['color'], opacity=1, name=mesh['name']))
    fig.update_layout(scene=dict(aspectmode="data", xaxis_title="X", yaxis_title="Y", zaxis_title="Z"), height=560, margin=dict(l=0,r=0,t=25,b=0))
    st.plotly_chart(fig, use_container_width=True)
    obj_text = "# PolyGen Group 8 procedural prototype OBJ\n" + "\n".join(mesh['obj'] for mesh in meshes)
    st.download_button("Download OBJ file", data=obj_text, file_name="polygen_asset.obj", mime="text/plain")
    st.success("Prototype mesh generated. Geometry is procedural and rule-based, not AI-generated.")
