import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("コロナによる影響")

df = pd.read_csv('country_covid_status.csv')
df = df.rename(columns={'New_cases':'感染者数', 'New_deaths':'死亡者数','population':'人口',
                        'deaths_by_cases':'死亡率', 'gdp_per_capita':'一人当たりのGDP'})

option = st.selectbox('国の選択', df['Country'])
st.write(option, 'を選びました。')

st.write(df[df['Country']==option][['人口', '感染者数', '死亡者数', '死亡率', '一人当たりのGDP']])

df_covid = pd.read_csv('covid_data.csv')

st.write(df_covid[df_covid['Country']==option])

def plot_new_cases_and_deaths_of_country(df,country):

    df['Date_reported'] = pd.to_datetime(df['Date_reported'])
    df2 = df[df["Country"] == country]
    fig, ax= plt.subplots(2,figsize= (20, 7))
    ax[0].plot(df2["Date_reported"], df2["New_cases"])
    ax[1].plot(df2["Date_reported"], df2["New_deaths"], color= "r")
    return fig
st.write(plot_new_cases_and_deaths_of_country(df_covid,option))

