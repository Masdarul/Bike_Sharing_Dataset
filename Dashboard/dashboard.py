import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul 
st.title('Dashboard Rental Sepeda 🚲')
st.markdown("---")
# Menyiapkan data day
day_df = pd.read_csv("Masdarul/Bike_Sharing_Dataset/Dashboard/dashboard.py")
day_df.head()

# Menghapus kolom tidak penting 
drop_col = ['instant', 'windspeed']

for i in day_df.columns:
  if i in drop_col:
    day_df.drop(labels=i, axis=1, inplace=True)

# Mengubah nama judul kolom
day_df.rename(columns={
    'dteday': 'Dateday',
    'yr': 'Year',
    'mnth': 'Month',
    'weathersit': 'Weather_Cond',
    'cnt': 'Count'
},inplace=True)

# Mengubah angka menjadi keterangan
day_df['Month'] = day_df['Month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['Weather_Cond'] = day_df['Weather_Cond'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})
# Mengubah tipe data ke datetime
day_df['Dateday'] = pd.to_datetime(day_df.Dateday)

# Mengubaha tipe data ke categorical
day_df['season'] = day_df.season.astype('category')
day_df['Year'] = day_df.Year.astype('category')
day_df['Month'] = day_df.Month.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['Weather_Cond'] = day_df.Weather_Cond.astype('category')

# Menyiapkan daily_rent_df
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='Dateday').agg({
        'Count': 'sum'
    }).reset_index()
    return daily_rent_df

# Menyiapkan daily_casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='Dateday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Menyiapkan daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='Dateday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
# Menyiapkan season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

# Menyiapkan monthly_rent_df
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='Month').agg({
        'Count': 'sum'
    })
    ordered_months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    monthly_rent_df = monthly_rent_df.reindex(ordered_months, fill_value=0)
    return monthly_rent_df

# Menyiapkan weekday_rent_df
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'Count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Menyiapkan workingday_rent_df
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'Count': 'sum'
    }).reset_index()
    return workingday_rent_df

# Menyiapkan holiday_rent_df
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'Count': 'sum'
    }).reset_index()
    return holiday_rent_df

# Menyiapkan weather_rent_df
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='Weather_Cond').agg({
        'Count': 'sum'
    })
    return weather_rent_df

# Membuat komponen filter
min_date = pd.to_datetime(day_df['Dateday']).dt.date.min()
max_date = pd.to_datetime(day_df['Dateday']).dt.date.max()


with st.sidebar:

    st.image('Masdarul/Bike_Sharing_Dataset/Dashboard/img/Logo.png')
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

    st.sidebar.header("Visit my Profile:")

    st.sidebar.markdown("Masdarul Rizqi")

    col1, col2 = st.sidebar.columns(2)
    # membuat link 
    with col1:
        st.markdown("[![LinkedIn](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/masdarul-rizqi-46ba17249/)")
    with col2:
        st.markdown("[![Github](https://img.icons8.com/glyph-neue/64/FFFFFF/github.png)](https://github.com/Masdarul)")


main_df = day_df[(day_df['Dateday'] >= str(start_date)) & 
                (day_df['Dateday'] <= str(end_date))]

# Menyiapkan berbagai dataframe
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)

# Membuat jumlah penyewaan harian
st.subheader('Sewa Harian')
col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Pengguna Biasa', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Pengguna Terdaftar', value= daily_rent_registered)
 
with col3:
    daily_rent_total = daily_rent_df['Count'].sum()
    st.metric('Jumlah Pengguna', value= daily_rent_total)

# Membuat jumlah penyewaan bulanan
st.subheader('Sewa Bulanan')
fig, ax = plt.subplots(figsize=(25, 7))
ax.plot(
    monthly_rent_df.index,
    monthly_rent_df['Count'],
    marker='o', 
    linewidth=2,
)

plt.xlabel("Bulan", fontsize=19)
plt.ylabel("Jumlah Sewa Sepeda", fontsize=19)

for index, row in enumerate(monthly_rent_df['Count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

# Membuat jumlah penyewaan berdasarkan season
st.subheader('Sewa Musiman')

fig, ax = plt.subplots(figsize=(15, 7))

sns.barplot(
    x='season',
    y='registered',
    data=season_rent_df,
    label='Pengguna Terdaftar',
    color='blue',
    ax=ax
)

sns.barplot(
    x='season',
    y='casual',
    data=season_rent_df,
    label='Pengguna Biasa',
    color='orange',
    ax=ax
)


for index, row in season_rent_df.iterrows():
    ax.text(index, row['registered'], str(row['registered']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['casual'], str(row['casual']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel('Musim',fontsize=15)
ax.set_ylabel('Jumlah Sewa Sepeda', fontsize=15)
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

# Membuah jumlah penyewaan berdasarkan kondisi cuaca
st.subheader('Penyewaan Cuaca')

fig, ax = plt.subplots(figsize=(15, 7))

palette=["blue", "orange", "green"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['Count'],
    palette=palette,
    ax=ax
)

for index, row in enumerate(weather_rent_df['Count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel('Kondisi Cuaca',fontsize=15)
ax.set_ylabel('Jumlah Pengguna Sepeda',fontsize=15)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

# Membuat jumlah penyewaan berdasarkan Sewa Hari Kerja, Hari Kerja, dan Hari Libur
st.subheader('Sewa Hari Kerja, Hari Kerja, dan Hari Libur')

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15,10))

colors = sns.color_palette("husl", n_colors=7)
Color = ['blue', 'skyblue']

# Berdasarkan workingday
sns.barplot(
    x='Hari Kerja',
    y='Count',
    data=workingday_rent_df,
    palette=Color,
    ax=axes[0])

for index, row in enumerate(workingday_rent_df['Count']):
    axes[0].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[0].set_title('Jumlah Sewa berdasarkan Hari Kerja')
axes[0].set_ylabel('Jumlah')
axes[0].set_xlabel('Hari Kerja')
axes[0].tick_params(axis='x', labelsize=15)
axes[0].tick_params(axis='y', labelsize=10)

# Berdasarkan Hari libur
sns.barplot(
  x='holiday',
  y='Count',
  data=holiday_rent_df,
  palette=Color,
  ax=axes[1])

for index, row in enumerate(holiday_rent_df['Count']):
    axes[1].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[1].set_title('Jumlah Sewa berdasarkan Hari Libur')
axes[1].set_ylabel('Jumlah')
axes[1].set_ylabel('Hari Libur')
axes[1].tick_params(axis='x', labelsize=15)
axes[1].tick_params(axis='y', labelsize=10)

# Berdasarkan Hari kerja
sns.barplot(
  x='weekday',
  y='Count',
  data=weekday_rent_df,
  palette=colors,
  ax=axes[2])

for index, row in enumerate(weekday_rent_df['Count']):
    axes[2].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[2].set_title('Jumlah Sewa berdasarkan Hari Kerja')
axes[2].set_ylabel('Jumlah')
axes[2].set_ylabel('Hari Kerja')
axes[2].tick_params(axis='x', labelsize=15)
axes[2].tick_params(axis='y', labelsize=10)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.markdown("""
    <div style="text-align: center;">
        <h3 style="color: #007BFF; font-weight: bold; animation: moveUp 2s ease infinite;">Copyright &copy; Masdarul Rizqi 2024</h3>
        <style>
            @keyframes moveUp {
                0%, 100% {
                    transform: translateY(0);
                }
                50% {
                    transform: translateY(-10px);
                }
            }
        </style>
    </div>
""", unsafe_allow_html=True)
