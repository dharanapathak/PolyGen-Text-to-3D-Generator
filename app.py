"""Streamlit interface for the PolyGen procedural 3D asset prototype."""

import re

import plotly.graph_objects as go
import streamlit as st

from src.prompt_processor import process_prompt
from src.primitive_generator import build_asset


st.set_page_config(
    page_title="PolyGen | Group 8",
    page_icon="🧊",
    layout="wide",
)

st.title("🧊 PolyGen — Text-to-3D Asset Pipeline")
st.caption("Generative AI internship prototype • Group 8 • Infotact Solutions")
st.info(
    "This prototype interprets prompts for supported primitive shapes and builds "
    "procedural 3D geometry. It is not yet connected to an AI text-to-3D model."
)

with st.sidebar:
    st.header("Supported objects")
    st.markdown("- Cube / box / block\n- Sphere / ball / globe\n- Cylinder / tube\n- Cone\n- Simple multi-part robot")
    st.caption("Recognized colour words include red, blue, green, yellow, orange, purple, pink, black and white.")

prompt = st.text_area(
    "Describe a 3D object",
    placeholder="e.g., a blue robot or a red cube",
    height=110,
)

generate_clicked = st.button(
    "Generate prototype asset",
    type="primary",
    disabled=not prompt.strip(),
)

if generate_clicked:
    try:
        parsed = process_prompt(prompt)

        if not parsed["supported"]:
            st.warning(
                "I could not identify a supported shape. Try cube, sphere, "
                "cylinder, cone, or robot."
            )
        else:
            meshes = build_asset(parsed)

            st.subheader("Prompt analysis")
            col1, col2, col3 = st.columns(3)
            col1.metric("Detected shape", parsed["shape"].title())
            col2.metric("Detected colour", parsed["color"].title())
            col3.metric("Detected material", parsed["material"].title())
            if parsed["color"] == "not specified":
                st.caption("No colour keyword was found; a default blue display colour is used.")
            st.write(f"**Processed description:** {parsed['description']}")

            figure = go.Figure()
            for mesh in meshes:
                figure.add_trace(
                    go.Mesh3d(
                        x=mesh["x"],
                        y=mesh["y"],
                        z=mesh["z"],
                        i=mesh["i"],
                        j=mesh["j"],
                        k=mesh["k"],
                        color=parsed["display_color"],
                        opacity=1.0,
                        name=mesh["name"],
                        flatshading=True,
                        showscale=False,
                    )
                )

            figure.update_layout(
                scene={
                    "aspectmode": "data",
                    "xaxis_title": "X",
                    "yaxis_title": "Y",
                    "zaxis_title": "Z",
                },
                height=560,
                margin={"l": 0, "r": 0, "t": 25, "b": 0},
                showlegend=False,
            )
            st.plotly_chart(figure, use_container_width=True)

            # Each mesh OBJ fragment uses globally offset face indices, so the
            # fragments can be concatenated into one valid multi-object OBJ.
            obj_text = (
                "# PolyGen procedural prototype OBJ\n"
                + "\n".join(mesh["obj"] for mesh in meshes)
                + "\n"
            )
            safe_shape = re.sub(r"[^a-z0-9_-]+", "_", parsed["shape"].lower()).strip("_")
            st.download_button(
                "Download OBJ file",
                data=obj_text,
                file_name=f"polygen_{safe_shape or 'asset'}.obj",
                mime="text/plain",
            )
            st.success(
                "Procedural prototype geometry generated. This is rule-based geometry, "
                "not an AI-generated 3D model."
            )

    except (TypeError, ValueError) as error:
        st.error(str(error))
    except Exception as error:  # Keep unexpected UI failures visible without crashing silently.
        st.exception(error)
