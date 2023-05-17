import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


def Abby_data():
    GloFood= "global_food_prices.csv"
    GloFood= pd.read_csv(GloFood)
    GloFood.rename(columns={
                     GloFood.columns[0]:'Country_id',
                     GloFood.columns[1]:'Country_name',
                     GloFood.columns[2]:'Locality_id',
                     GloFood.columns[3]:'Locality_name',
                     GloFood.columns[4]:'Market_id',
                     GloFood.columns[5]:'Market_name',
                     GloFood.columns[6]:'Commodity_purchase_id',
                     GloFood.columns[7]:'Commodity_purchased',
                     GloFood.columns[8]:'Currency_id',
                     GloFood.columns[9]:'Currency_name',
                     GloFood.columns[10]:'Market_type_id',
                     GloFood.columns[11]:'Market_type',
                     GloFood.columns[12]:'Measurement_id',
                     GloFood.columns[13]:'Unit_measurement',
                     GloFood.columns[14]:'Month',
                     GloFood.columns[15]:'Year',
                     GloFood.columns[16]:'Price',
                     GloFood.columns[17]:'Commodity_source',
}, inplace=True)
     # dropping empty column
    GloFood.drop(['Commodity_source'], axis=1, inplace=True)
    
    # remove the duplicate names on the lists
    items=[]
    for item_name in list(GloFood.Commodity_purchased.str.split('-')):
        items.append(item_name[0])
    GloFood.Commodity_purchased=items
    return GloFood


GloFood = Abby_data()
st.title("Global Food Prices ABIODUN E OJO REPORT")
st.write(GloFood.head(50))
food=['Country_name', 'Commodity_purchased', 'Price', 'Year']
GloFood[food].value_counts().sort_values(ascending=False)
# view specific country selected by user
grp_country = GloFood.groupby('Country_name')
# side bar
with st.sidebar:
    st.subheader('pick a country to view more details')
    selected_country =st.selectbox('select a country',list(GloFood.Country_name.unique()))
selected_country_details =grp_country.get_group(selected_country)
st.subheader(selected_country)
st.write(selected_country_details[['Country_name', 'Commodity_purchased', 'Currency_name', 'Market_type', 'Unit_measurement','Year', 'Price']].head(10))
if selected_country:
    
    with st.sidebar:
        st.subheader('pick a Commodity')
        comm=st.multiselect('select Commodity_purchased', list(GloFood.Commodity_purchased.unique()))
    used_selected_comm= selected_country_details['Commodity_purchased'].str.split(';')
    temp=st.write(used_selected_comm)
    
    with st.sidebar:
        st.subheader('pick a Locality')
        comm=st.multiselect('select Localiy_name', list(GloFood.Locality_name.unique()))
    used_selected_local= selected_country_details['Locality_name'].str.split(';')
    temp=st.write(used_selected_local)
    
    with st.sidebar:
        st.subheader('pick a Market')
        comm=st.multiselect('select Market_name', list(GloFood.Market_name.unique()))
    used_selected_mar= selected_country_details['Market_name'].str.split(';')
    temp=st.write(used_selected_mar)
    
    with st.sidebar:
        st.subheader('pick a Year')
        year=st.multiselect('select Year', list(GloFood.Year.unique()))
    used_selected_year= selected_country_details['Year']
    temp=st.write(used_selected_year)
    
    with st.sidebar:
        st.subheader('pick a Price')
        price=st.multiselect('select Price', list(GloFood.Price.unique()))
    used_selected_price= selected_country_details['Price']
    temp=st.write(used_selected_price)
    
else:
    pass
st.write(
"""### Top 10 Countries"""
)
pie_data= GloFood['Country_name'].value_counts().head(10)
fig1, ax1 = plt.subplots(figsize=(10,8))
ax1.pie(pie_data, labels=pie_data.index, autopct="%1.1f&&")
# display the figure and pie chart
st.pyplot(fig1)
st.write(
"""### Top 10  Commodity Purchased from Countries in percentage"""
)
pie_data= GloFood['Commodity_purchased'].value_counts().head(10)
fig1, ax1 = plt.subplots(figsize=(10,8))
ax1.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
st.pyplot(fig1)

# bar chart
st.write(
   """## Mean Price of Commodities by Country"""
)
bar_data = GloFood.groupby(['Country_name'])['Price'].mean().sort_values(ascending=True).head(10)
st.bar_chart(bar_data)



