import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(layout="wide", page_title="Tampilan Data Excel", page_icon="📄")

st.title("📄 Data Training")

# Path file
path = r"D:\Tubes_Mosi\Tubes_Mosi.xlsx"  

# Fungsi untuk memuat data dari Excel
@st.cache_data
def load_excel_data(path):
    try:
        df = pd.read_excel(path, sheet_name="DataTrain")
        return df
    except FileNotFoundError:
        st.error(f"❌ File tidak ditemukan di: {path}")
        return pd.DataFrame()
    except ValueError as e:
        st.error(f"❌ Gagal membaca sheet: {e}")
        return pd.DataFrame()

# Load data
df = load_excel_data(path)

# Tampilkan data jika berhasil dimuat
if not df.empty:
    st.subheader("📊 Data dari Sheet 'DataTrain'")
    st.dataframe(df)
else:
    st.warning("Tidak ada data yang bisa ditampilkan.")
