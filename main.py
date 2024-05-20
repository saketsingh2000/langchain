
#streamlit allows us to build POC applications quickly


import streamlit as st
import langchain_add

st.title("Restaurant Name Generator")
cuisine= st.sidebar.selectbox("Pick a Cuisine", ("Indian","Italian","Mexican","Chinese", "Arabic","American"))



if cuisine:
    response=langchain_add.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(',')

    st.write("Menu Items")

    for item in menu_items:
        st.write("-",item)