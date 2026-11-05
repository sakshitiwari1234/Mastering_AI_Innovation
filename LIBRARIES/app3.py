import pandas as pd
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# import streamlit as st
from PIL import Image

# Load dataset
amazon_df = pd.read_csv(r"C:\Users\Lenovo\Downloads\amazon_product.csv")

print(amazon_df.head())
amazon_df.info()

# Drop unnecessary columns
amazon_df.drop('id', axis=1, inplace=True)

# Download NLTK punkt tokenizer
import nltk
nltk.download('punkt')

# Tokenization and stemming function
stemmer = nltk.stem.SnowballStemmer("english")

def tokenize_stem(text):
    tokens = nltk.word_tokenize(text.lower())
    stemmed = [stemmer.stem(w) for w in tokens]
    return " ".join(stemmed)

# Preprocess columns
amazon_df['stemmed_tokens'] = amazon_df.apply(lambda row: row['Title'] + " " + row['Description'], axis=1)

# TF-IDF Vectorizer
tfdiv = TfidfVectorizer()

def cosine_sim(txt1, txt2):
    matrix = tfdiv.fit_transform([txt1, txt2])
    return cosine_similarity(matrix)[0, 1]

# Product search function
def search_product(query):
    stemmed_query = tokenize_stem(query)
    amazon_df['similarity'] = amazon_df['stemmed_tokens'].apply(lambda x: cosine_sim(stemmed_query, x))
    res = amazon_df.sort_values(by=['similarity'], ascending=False).head(10)[['Title', 'Description', 'Category']]
    return res

# Test product search
print(search_product('PURELL ES8 Professional HEALTHY SOAP Foam Refill, Fresh Scent Fragrance'))


# Load and display image
# img = Image.open(r'C:\Users\Lenovo\Downloads\amazon_photo_final.jpg')
# st.image(img, width=600)
# st.title("Search Engine and Product Recommendation System")
