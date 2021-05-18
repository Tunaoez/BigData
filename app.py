import streamlit as st
import requests
import json
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


# Draw a title and some text to the app:
st.title("People in Space & ISS Current Location")
st.write("This app provides an overview about people who are in _space_ righ now")

#people in space
space = requests.get("http://api.open-notify.org/astros.json/")
data = json.loads(space.text)
nr = data["number"]

st.write("Number of people in space right now is" + " " + str(nr) + ".")
st.write("The names of those people are:")

for item in data["people"]:
    st.write((item["name"]))

# -------------------------PLOT SIMPLE MAP----------------------------

# Location
url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)

# Create new column called latitude and longitude and drop index and message
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True) 
df = df.drop(['index', 'message'], axis=1)

# Plot 
fig = px.scatter_geo(data_frame=df, lat='latitude', lon='longitude')
fig.show()
