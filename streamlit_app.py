#import libraries
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding titlekkk
st.title("Title Here")

#adding discription to your website
st.text('Discription')

#Thesis here
st.header('Thesis')
st.text('Add your Thesis here')

#SHOWING THE DATA
#dataset Header
st.header('Dataset')

#add your dataset (delete dataset this is an example)
BostonHousing = pd.read_csv("BostonHousing.csv")

#showing dataset
st.table(BostonHousing.head())
st.text('Showing dataset and writting about it here')

#Adding images to make your streamlit look visually better!
st.image('pro.png')
st.text('You can add photos with descriptions')

#Adding 3-6 Visualizations using photos collected and made from your graph
#adding images
#adding graphs by images
st.image('pasted image 0.png')
st.text('Discription about your graph and visualizations')

#adding graphs by making plotly_Chart
# Plot!
#st.plotly_chart(BostonHousing, use_container_width=True)
#st.text('Discription')

#adding conclusions
st.header('Conclusion')
st.text('add your conclusion here')

import streamlit as st
import plotly.express as px

# Sample data
df = px.data.iris()

# Plot
fig = px.scatter(df,
                 x="sepal_width",
                 y="sepal_length",
                 color="species",
                 size='petal_length',
                 hover_data=['petal_width'])

st.title('Iris dataset')
st.plotly_chart(fig)
