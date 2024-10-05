import streamlit as st
import pandas as pd
import pickle
import numpy as np

 
df = pd.read_csv(r"final_bus.csv")

model = pickle.load(open(r"knn.pkl","rb"))

df = df.drop(columns=['Unnamed: 0'], errors='ignore')

st.image(r"ino_img.jpg")

st.title("PREDICTING PRICE'S")
st.header("BUS BOOKING INFORMATION")

# State Selection
state = st.selectbox("Select State", df['State'].unique())

# Filter data by selected state
filtered_data = df[df['State'] == state]

# Route Selection
route = st.selectbox("Select Route", filtered_data['From_To'].unique())

route_data = filtered_data[filtered_data['From_To'] == route]

pickup = st.selectbox("Select PickUp Point", route_data['PickUp'].unique())

drop = st.selectbox("Select Drop Point", route_data['Drop'].unique())

bus_name = st.selectbox("Select Name of Bus",route_data["Bus_Name"].unique())

bus_type = st.selectbox("Select Bus Type", route_data['Bus_Type'].unique())

rating = st.selectbox("Select Rating", sorted(route_data['Rating'].unique()))



price = route_data[(route_data['PickUp'] == pickup) & 
                   (route_data['Drop'] == drop) & 
                   (route_data['Bus_Type'] == bus_type) &
                   (route_data['Bus_Name'] == bus_name) & 
                   (route_data['Rating'] == rating)]['Price']



if st.button("Submit"):
    
    price = model.predict([[pickup, drop, bus_type, bus_name, route, rating, state]])
    
    st.success(f"Ticket Price:-  ₹{price[0]}")
