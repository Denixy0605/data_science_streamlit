import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('country_covid_status.csv')

st.title("GDPと死亡率の相関")


#plt.rcParams['font.family'] = 'MS Gothic'

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(df['gdp_per_capita'], df['deaths_by_cases'], 'o')
#ax.set_xlabel('一人当たりのGDP（USドル）')

st.write(fig)
st.write('相関係数の値')
st.write(df['deaths_by_cases'].corr(df['gdp_per_capita']))
st.write(df)
