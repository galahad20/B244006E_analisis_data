import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import altair as alt


#set page layout
st.set_page_config(
    page_title="B244006E Bike-sharing dashboard",
    page_icon=":bar_chart:",
    layout="wide"
    )


#load_dataset csv
@st.cache_data
def load_csv(path: str):
    data = pd.read_csv(path)
    return data

df_hari = load_csv("data/day.csv")
df_jam = load_csv("data/hour.csv")


#data-cleaning

#drop instant feature
grupDF = [df_hari,df_jam]
for i in grupDF:
    i.drop(labels='instant', axis=1, inplace=True)

#rename feature into understable one at a glance
for i in grupDF:
  i.rename(columns={
      'dteday': 'date',
      'yr': 'year',
      'mnth': 'month',
      'temp': 'temperature',
      'hum': 'humidity',
      'cnt': 'count'
  }, inplace = True)

#rename year detail in year feature
for i in grupDF:
    i['year'] = i['year'].map({
        0: '2011',
        1: '2012'
    })
#rename season detail in season feature
for i in grupDF:
    i['season'] = i['season'].map({
        1: 'spring',
        2: 'summer',
        3: 'fall',
        4: 'winter'
    })
#rename month detail in month feature
for i in grupDF:
    i['month'] = i['month'].map({
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    })

#rename weekday detail in weekday feature
for i in grupDF:
    i['weekday'] = i['weekday'].map({
        0: 'sunday',
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday'
    })

#rename weather situation in wethersit feature
for i in grupDF:
    i['weathersit'] = i['weathersit'].map({
        1: 'Clear / Few clouds',
        2: 'Mist / Cloudy',
        3: 'Light rain / Light snow',
        4: 'Heavy rain / Heavy snow'
    })

#change data type for date from obj to datetime
for i in grupDF:
  i['date'] = pd.to_datetime(i['date'])




#make date filter
min_date = df_hari['date'].dt.date.min()
max_date = df_hari['date'].dt.date.max()

#make sidebar
with st.sidebar:
    st.header("Filter")
    #make input date
    default_start_date = min_date
    default_end_date = max_date
    start_date = st.date_input("Start date", default_start_date, min_value= min_date, max_value= max_date)
    end_date = st.date_input("End date", default_end_date, min_value= min_date, max_value= max_date)


#define variable & function needed for visualization

    #df_main will be the main dataframe used in this dashboard
    df_main = df_hari[(df_hari['date'] >= str(start_date)) & (df_hari['date'] <= str(end_date))]
    
    #define function
    
    #create total, casual, registered user variable in a day
    total_userByDay = df_main.groupby(['date']).agg({'count': 'sum'})
    casual_userByDay = df_main.groupby(['date']).agg({'casual': 'sum'})
    registered_userByDay = df_main.groupby(['date']).agg({'registered': 'sum'})
    
    #create variable for chart
    #userByMonth = df_main.groupby(['month']).agg({'count': 'mean','casual': 'mean','registered': 'mean'})
    userByMonth2 = df_main.groupby(['month']).agg({'count': 'sum','casual': 'sum','registered': 'sum'})
    
    userBySeason = df_main.groupby(['season']).agg({'count': 'sum','casual': 'sum','registered': 'sum'})
    userByWeek = df_main.groupby(['weekday']).agg({'count': 'sum','casual': 'sum','registered': 'sum'})
    
    #not yet fixed x axis on line chart
    
#setting dashboard layout
col = st.columns((1.5, 4, 1.5), gap='medium')


with col[0]:
    st.markdown('#### Count ')
    
    #metric for first column
    st.metric('Total User', value= total_userByDay.sum())
    st.metric('Casual User', value= casual_userByDay.sum())
    st.metric('Registered User', value= registered_userByDay.sum())


with col[1]:
    #title
    st.subheader('Dashboard Bike-sharing 2011-2012')
    st.markdown("ver 1.0")
    
    #show_or_not preview ahaahha
    with st.expander("Data preview"):
        st.dataframe(df_hari)
        
    #metric for second column
    st.subheader("Rent in a season")
    st.line_chart(userBySeason)
    st.subheader("Rent in a month")
    st.line_chart(userByMonth2)
    st.subheader("Rent in a week")
    st.line_chart(userByWeek)
with col[2]:
    st.subheader('About dashboard')
    st.text("Bike-sharing from 2011-2012")
    st.text("Dashboard ini berisi menampilkan pengguna penyewaan sepeda pada tahun 2011-2012. Ditampilkan dalam musim, bulan, dan minggu. Terdapat grafik yang menunjukkan jumlah pelanggan yang registered dan casual")
