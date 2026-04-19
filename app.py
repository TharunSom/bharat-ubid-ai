import streamlit as st
import pandas as pd
from src.entity_matching import match_entities
from src.ubid_generator import generate_ubid

st.title("🇮🇳 BharatUBID - AI Business Identity System")

# Load dataset
df = pd.read_csv("data/raw_data.csv")

st.subheader("📂 Input Data")
st.write(df)

if st.button("Generate UBID"):
    groups = match_entities(df)
    ubid_map = generate_ubid(groups)

    df['UBID'] = df.index.map(ubid_map)

    st.subheader("✅ Processed Data with UBID")
    st.write(df)

    st.subheader("📊 Total Unique Businesses")
    st.write(df['UBID'].nunique()
