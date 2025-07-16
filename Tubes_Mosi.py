import streamlit as st
import pandas as pd

st.set_page_config(page_title="Google Sheet Viewer", layout="wide")

st.title("📄 Data dari Google Sheets - Sheet: DataTrain")

# Ganti ini dengan URL CSV hasil publish
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-.../pub?output=csv"  # Ganti dengan yang kamu dapat

@st.cache_data
def load_data_from_google_sheet(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return pd.DataFrame()

df = load_data_from_google_sheet(csv_url)

if not df.empty:
    st.subheader("📊 Data dari Google Sheet")
    st.dataframe(df)
else:
    st.warning("Data tidak tersedia.")
