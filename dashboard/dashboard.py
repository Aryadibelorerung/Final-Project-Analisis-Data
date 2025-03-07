import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur tema seaborn
sns.set_theme(style="dark")

# Fungsi untuk membuat DataFrame jumlah penyewaan harian oleh pengguna casual
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dateday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Fungsi untuk membuat DataFrame jumlah penyewaan harian oleh pengguna terdaftar (registered)
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dateday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df

# Fungsi untuk membuat DataFrame jumlah penyewaan harian secara keseluruhan
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dateday').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df
    
# Fungsi untuk membuat DataFrame jumlah penyewaan berdasarkan musim
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

# Fungsi untuk membuat DataFrame jumlah penyewaan berdasarkan bulan
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='month').agg({
        'count': 'sum'
    })
    ordered_months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    monthly_rent_df = monthly_rent_df.reindex(ordered_months, fill_value=0)
    return monthly_rent_df

# Fungsi untuk membuat DataFrame jumlah penyewaan berdasarkan hari dalam seminggu
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='day_of_week').agg({
        'count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Fungsi untuk mendapatkan jumlah total penyewaan berdasarkan jam
def get_total_count_by_hour_df(hour_df):
  hour_count_df =  hour_df.groupby(by="hour").agg({"count": ["sum"]})
  return hour_count_df

# Fungsi untuk membuat DataFrame jumlah penyewaan berdasarkan hari libur
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'count': 'sum'
    }).reset_index()
    return holiday_rent_df


# Fungsi untuk membuat DataFrame jumlah penyewaan berdasarkan tahun
def create_year_rent_df(df):
    year_rent_df = df.groupby(by='year').agg({
        'count': 'sum'
    })
    return year_rent_df

# Membaca dataset harian dan per jam
day_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")

# Konversi kolom tanggal ke tipe datetime
datetime_columns = ["dateday"]
day_df.sort_values(by="dateday", inplace=True)
day_df.reset_index(inplace=True)   

for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])

# Menentukan rentang tanggal minimum dan maksimum untuk filter
min_date_days = day_df["dateday"].min()
max_date_days = day_df["dateday"].max()

min_date_hour = hour_df["dateday"].min()
max_date_hour = hour_df["dateday"].max()

# Sidebar untuk memilih rentang waktu dengan logo perusahaan
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://st4.depositphotos.com/1588812/26966/v/450/depositphotos_269662818-stock-illustration-logo-for-bicycle-rental-vector.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days])

# Menyaring data berdasarkan rentang waktu yang dipilih oleh pengguna
main_df_days = day_df[(day_df["dateday"] >= str(start_date)) & (day_df["dateday"] <= str(end_date))]
main_df_hour = hour_df[(hour_df["dateday"] >= str(start_date)) & (hour_df["dateday"] <= str(end_date))]


# Menyiapkan berbagai DataFrame berdasarkan data yang sudah difilter
daily_casual_rent_df = create_daily_casual_rent_df(main_df_days)
daily_registered_rent_df = create_daily_registered_rent_df(main_df_days)
daily_rent_df = create_daily_rent_df(main_df_days)
season_rent_df = create_season_rent_df(main_df_days)
monthly_rent_df = create_monthly_rent_df(main_df_days)
hour_count_df = get_total_count_by_hour_df(main_df_hour)
weekday_rent_df = create_weekday_rent_df(main_df_days)
holiday_rent_df = create_holiday_rent_df(main_df_days)


# Membuat Dashboard

# Membuat judul dashboard
st.title('Dashboard Penyewaan Sepeda 🚴')

# Judul Aplikasi Streamlit
st.header("Analisis Penyewaan Sepeda Bulanan")

# Menampilkan jumlah penyewaan harian berdasarkan kategori pengguna
st.subheader('Peminjaman Harian')
col1, col2, col3 = st.columns(3)
 
with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Casual User', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Registered User', value= daily_rent_registered)
 
with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.metric('Total User', value= daily_rent_total)

# Memuat dataset dengan caching agar lebih cepat
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/day_clean.csv")
    return df

day_df = load_data()

day_df['month'] = pd.Categorical(day_df['month'], categories=
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ordered=True)

# Mengelompokkan data berdasarkan bulan dan tahun
monthly_counts = day_df.groupby(by=["month", "year"], observed=False).agg({
    "count": "sum"
}).reset_index()

# Membuat visualisasi dengan matplotlib dan seaborn
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.header("Pertanyaan 1")
    #Pertanyaan 1
    st.subheader("Bagaimana tren pertumbuhan penjualan perusahaan dalam 2 tahun terakhir?")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        data=monthly_counts,
        x="month",
        y="count",
        hue="year",
        palette="pastel",
        marker="o",
        ax=ax
    )

    ax.set_title("Total Penyewaan Sepeda per Bulan dalam Setiap Tahun")
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.legend(title="Tahun", loc="upper right")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
 
with tab2:
    st.header("Pertanyaan 2")
    #Pertanyaan 2
    st.subheader("Perbandingan Customer yang Registered dengan casual")

    labels = 'casual', 'registered'
    sizes = [18.8, 81.2]
    explode = (0.05, 0) 

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',colors=["#FFDAB9", "#87CEFA"])
    ax1.axis('equal')  

    st.pyplot(fig1)
 
with tab3:
    st.header("Pertanyaan 3")
    #Pertanyaan 3
    st.subheader("Musim Apa yang Paling Banyak Disewa?")

    # Tentukan urutan musim yang benar
    season_order = ["Spring", "Summer", "Fall", "Winter"]

    day_df["season"] = pd.Categorical(day_df["season"], categories=season_order, ordered=True)

    # Warna chart
    colors = ["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3"]

    # Buat plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(
        y="count", 
        x="season",
        data=day_df.sort_values(by="season"),  # Pastikan tetap mengikuti urutan kategori
        palette=colors,
        ax=ax
    )

    ax.set_title("Grafik Antar Musim", loc="center", fontsize=20)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)

    # Tampilkan di Streamlit
    st.pyplot(fig)

# end