import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import psycopg2
import time

data = pd.read_csv('amziaus_grupes.csv')
df = pd.DataFrame(data)
# print(df

