# PhyscialAI.py

import streamlit as st
import pandas as pd
from PIL import Image


pg = st.navigation([st.Page("🧠Physical AI.py"), st.Page("🤖Dashboard.py")])
pg.run()


st.sidebar.header("Global commercial real estate services")
image = Image.open("logo.png")
st.sidebar.image(image)