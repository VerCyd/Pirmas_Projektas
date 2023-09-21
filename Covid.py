import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import psycopg2
import time
# data = pd.read_csv('C:/Users/kesta/OneDrive/Desktop/covid')
# df = pd.DataFrame(data)

data = pd.read_csv('covid.csv')
df = pd.DataFrame(data)
print(df)

