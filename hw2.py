import streamlit as st
import seaborn as sns
import plotly.express as px
iris_data = sns.load_dataset("iris")
print(iris_data.columns)
st.write("""
Iris Dataset
How are petal and sepal's attributes correlated in Iris species?
""")
py_handle = px.scatter_3d(iris_data, x='petal_length', y='petal_width', z='sepal_length', size='sepal_width', color='species')
st.plotly_chart(py_handle)