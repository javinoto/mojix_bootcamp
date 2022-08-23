import streamlit as st
import pandas as pd
import urllib
import csv
# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly_express as px 

# Title

st.set_page_config(
    page_title = 'Discrepancy Dashboard',
    page_icon = ':bar_chart:',
    layout = 'wide'
)

# ---- Table ----
df = pd.read_csv('./data.csv')


# ---- SIDEBAR ----

st.sidebar.header("FILTER: ")

Product = st.sidebar.multiselect(
    'Select Retail Product: ',
    options = df['Retail_Product_Level1Name'].unique(),
    default = df['Retail_Product_Level1Name'].unique()
)

Color = st.sidebar.multiselect(
    'Select Color: ',
    options = df['Retail_Product_Color'].unique(),
    default = df['Retail_Product_Color'].unique()
)

df_selection = df.query(
    'Retail_Product_Level1Name == @Product & Retail_Product_Color == @Color'
)

# st.dataframe(df_selection)



# ---- MAINPAGE ----
st.title(':bar_chart: Retail Dashboard')
st.markdown('##')

# ---- DATA ----
expected = int(df_selection['Retail_SOHQTY'].sum())
counted = int(df_selection['Retail_CCQTY'].sum())
discrepancy = int(df_selection['Unders'].sum())

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Total Expected:')
    st.subheader(f'Und {expected:}')
with middle_column:
    st.subheader('Total Counted:')
    st.subheader(f'Und {counted:}')
with right_column:
    st.subheader('Under:')
    st.subheader(f'Und {discrepancy:}')

st.markdown('---')

st.dataframe(df_selection)
