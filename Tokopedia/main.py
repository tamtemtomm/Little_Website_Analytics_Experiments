import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

def read_csv(prompt):
    df = pd.read_csv(f"{prompt}product.csv").drop('Unnamed: 0', axis=1).set_index('name')
    print('Data berhasil di load')
    return df

def visual(df):
    # sold visual
    fig, ax = plt.subplots(figsize=(20,16))
    sns.countplot(df.sold, ax=ax)
    plt.xticks(rotation=90, fontsize=20)
    plt.yticks(rotation=90, fontsize=20)
    plt.xlabel('Sold', fontsize=25)
    plt.ylabel('Frequency', fontsize=25)
    fig.savefig('sold.jpg')
    
    # rating visual
    fig, ax = plt.subplots(figsize=(20,16))
    sns.countplot(df.rating, ax=ax)
    plt.xticks(rotation=90, fontsize=20)
    plt.yticks(rotation=90, fontsize=20)
    plt.xlabel('Rating', fontsize=25)
    plt.ylabel('Frequency', fontsize=25)
    fig.savefig('rating.jpg')
    
    # price visual
    fig, ax = plt.subplots(figsize=(20,16))
    sns.histplot(df.price, binwidth=50000, ax=ax)
    plt.xticks(rotation=90, fontsize=20)
    plt.yticks(rotation=90, fontsize=20)
    plt.xlabel('Price', fontsize=25)
    plt.ylabel('Frequency', fontsize=25)
    fig.savefig('price.jpg')
    
    # city visual
    fig, ax = plt.subplots(figsize=(25, 30))
    sns.countplot( df.city, orient = 'v', ax=ax)
    plt.xticks(rotation=90, fontsize=22)
    plt.yticks(rotation=90, fontsize=20)
    plt.xticks(rotation=90)
    plt.xlabel('City', fontsize=25)
    plt.ylabel('Frequency', fontsize=25)
    fig.savefig('city.jpg')
    
    print('Plot berhasil di ekspor')

def stream():
    st.title('Make a Simple Stats from Tokopedia Search')
    st.markdown("""
    * **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
    * **Data source:** Live Scraping using Selenium.
    """)
    
    # sold plot stream 
    sold = Image.open('sold.jpg')
    st.image(sold, caption='Plot produk terjual')
    print('Sold berhasil di muat')
    
    # rating plot stream 
    rating = Image.open('rating.jpg')
    st.image(rating, caption='Plot Rating Produk')
    print('Rating berhasil di muat')
    
    # price plot stream 
    price = Image.open('price.jpg')
    st.image(price, caption='Plot harga Produk')
    print('Price berhasil di muat')
    
    # city plot stream 
    city = Image.open('city.jpg')
    st.image(city, caption='Plot asal kota Produk')
    print('City berhasil di muat')
    
def main():
    prompt = input('Masukkan prompt : ')
    df  = read_csv(prompt)
    visual(df)
    stream()
    
    

if __name__ == '__main__':
    main()