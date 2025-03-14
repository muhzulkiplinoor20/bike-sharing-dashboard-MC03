import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk memuat data
def load_data():
    day_df = pd.read_csv("/content/drive/My Drive/MC03 Proyek Analisis Data/day.csv")
    hour_df = pd.read_csv("/content/drive/My Drive/MC03 Proyek Analisis Data/hour.csv")
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    return day_df, hour_df

# Load Data
day_df, hour_df = load_data()

# Sidebar
st.sidebar.title("Bike Sharing Dashboard")
page = st.sidebar.radio("Pilih Analisis:", ["Pengaruh Cuaca", "Pola Penyewaan Sepeda"])

# Judul Utama
st.title("Dashboard Analisis Bike Sharing")

if page == "Pengaruh Cuaca":
    st.header("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.boxplot(x='weathersit', y='cnt', data=day_df, ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Cuaca")
    st.pyplot(fig)

    st.write("**Insight:** Cuaca yang lebih buruk cenderung menurunkan jumlah penyewaan sepeda.")

elif page == "Pola Penyewaan Sepeda":
    st.header("Pola Penyewaan Sepeda Berdasarkan Jam")
    avg_hourly = hour_df.groupby('hr').mean().reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(x='hr', y='cnt', data=avg_hourly, ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_title("Pola Penyewaan Sepeda Berdasarkan Jam")
    st.pyplot(fig)

    st.write("**Insight:** Ada lonjakan penyewaan pada jam sibuk pagi dan sore hari.")

# Tambahkan footer
st.sidebar.markdown("---")
st.sidebar.text("Dibuat oleh: Muh. Zulkipli Noor Hermawan")
