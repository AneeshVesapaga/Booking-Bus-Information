import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the dataset
file_path = 'ABCD.csv'  # Update with the actual file path
df = pd.read_csv(r"C:\Users\anees\Data Analysis\Python\Redbus\ABCD.csv")

model = pickle.load(open(r"C:\Users\anees\Data Analysis\Python\Redbus\knn.pkl","rb"))

# Remove the unnamed column if necessary
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

# Filter data by selected route
route_data = filtered_data[filtered_data['From_To'] == route]

# PickUp Selection
pickup = st.selectbox("Select PickUp Point", route_data['PickUp'].unique())

# Drop Selection
drop = st.selectbox("Select Drop Point", route_data['Drop'].unique())

# Bus Type Selection
bus_type = st.selectbox("Select Bus Type", route_data['Bus_Type'].unique())

# Rating Selection
rating = st.selectbox("Select Rating", sorted(route_data['Rating'].unique()))



# Show ticket price if matching data is found
price = route_data[(route_data['PickUp'] == pickup) & 
                   (route_data['Drop'] == drop) & 
                   (route_data['Bus_Type'] == bus_type) & 
                   (route_data['Rating'] == rating)]['Price']

price = model.predict([[pickup,drop,bus_type,route,rating,state]])


st.write(f"Ticket Price: ₹{price}")

