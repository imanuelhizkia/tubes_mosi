import streamlit as st
import pandas as pd
import gdown

# Set halaman
st.set_page_config(page_title="Data Excel dari Google Drive", layout="wide")

st.title("📄 Data Excel dari Google Drive (Sheet: DataTrain)")

# ID File Google Sheets yang akan diunduh sebagai Excel (.xlsx)
file_id = "1hDpXpEXw91e6BAsaMt6xrwe_pEVxJlfX"  # Ganti sesuai milikmu
download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
local_filename = "Tubes_Mosi.xlsx"

# Fungsi load data
@st.cache_data
def load_excel_from_drive(url, filename):
    try:
        gdown.download(url, filename, quiet=False)
        df = pd.read_excel(filename, sheet_name="DataTrain")
        return df
    except Exception as e:
        st.error(f"❌ Gagal mengunduh atau membaca file: {e}")
        return pd.DataFrame()

# Load data
df = load_excel_from_drive(download_url, local_filename)

# Tampilkan
if not df.empty:
    st.subheader("📊 Data dari Sheet 'DataTrain'")
    st.dataframe(df)
else:
    st.warning("Tidak ada data yang ditampilkan.")
