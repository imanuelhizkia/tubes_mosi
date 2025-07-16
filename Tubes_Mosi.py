import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(layout="wide", page_title="Tampilan Data Excel", page_icon="📄")

st.title("📄 Tampilan Data Excel - Tubes_Mosi.xlsx (Sheet: DataTrain)")

# Fungsi untuk memuat data dari file Excel lokal
@st.cache_data
def load_excel_data():
    try:
        df = pd.read_excel("Tubes_Mosi.xlsx", sheet_name="DataTrain")
        return df
    except FileNotFoundError:
        st.error("❌ File 'Tubes_Mosi.xlsx' tidak ditemukan. Pastikan file berada di direktori yang sama.")
        return pd.DataFrame()
    except ValueError as e:
        st.error(f"❌ Gagal membaca sheet: {e}")
        return pd.DataFrame()

# Load data
df = load_excel_data()

# Tampilkan data jika tidak kosong
if not df.empty:
    st.subheader("📊 Data dari Sheet 'DataTrain'")
    st.dataframe(df)
else:
    st.warning("Tidak ada data yang ditampilkan.")
