import pandas as pd
import numpy as np
import streamlit as st
import calendar


df = pd.read_csv('accidents_2017.csv')

st.dataframe(df)