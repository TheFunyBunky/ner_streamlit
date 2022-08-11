import pathlib
import spacy
import os
import streamlit as st

directory = pathlib.Path(__file__).parent.resolve()

st.title("Food entities")

# path to folder where meta.json is located
nlp = spacy.load(os.path.join(directory, "v2"))


input_text = st.text_input('Text string to analyze:')

doc= nlp(input_text)

# dep_svg = spacy.displacy.render(doc, style="dep", jupyter=False)

# st.image(dep_svg, width=400, use_column_width='never')


st.header("Entity visualizer")

ent_html = spacy.displacy.render(doc, style="ent", jupyter=False)

st.markdown(ent_html, unsafe_allow_html=True)
