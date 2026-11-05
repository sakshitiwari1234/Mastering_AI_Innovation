# import pandas as pd
# import nltk
# import numpy as np

# from nltk.stem.snowball import SnowballStemmer
# # import scikit-learn
# import sklearn


# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import streamlit as st
# from PIL import Image

# amazon_df = pd.read_csv("C:/Users/Lenovo/Downloads/amazon_product.csv")
# # printing the favourite top five rows .
# print(amazon_df.head())
# amazon_df.info()

# #formalities....just
# amazon_df.drop('id', axis =1, inplace = True)

# amazon_df.isnull().sum()

# import nltk
# nltk.download('punkt')
# # just to check the working of nltk 
# nltk.sent_tokenize("i am a good boy, i am good what about youuuu")

# print('hello')
# # b using stemmer library code - to search for the keywords and storing it in stemmer variabl
# from nltk.stem.snowball import SnowballStemmer
# stemmer = SnowballStemmer("english")
# def tokenize_stem(text):
#   tokens = nltk.word_tokenize(text.lower())
#   stemmed = [stemmer.stem(w) for w in tokens]
#   return " ".join(stemmed)


# print(amazon_df.columns.str.strip())

# amazon_df['stemmed_tokens'] = amazon_df.apply(lambda row: row['Title'] + " " + row['Description'], axis=1)
# # after the tokeniziation of data (rows) - it is as follows look
# print(amazon_df.head())

# # sklearn library using to change to convert the statmenets of data into egrate the two statements entered by the user..
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_distances
# tfdiv = TfidfVectorizer(tokenizer = tokenize_stem)
# def cosine_sim(txt1, txt2):
#   txt1_concatenated = ' '.join(txt1)
#   txt2_concatenated = ' '.join(txt2)
#   matrix = tfdiv.fit_transform([txt1_concatenated, txt2_concatenated])
#   return matrix[0,1]


# def search_product(query):
#   stemmed_query = tokenize_stem(query)
#   amazon_df['similarity'] = amazon_df['stemmed_tokens'].apply(lambda x:cosine_sim(stemmed_query, x))
#   res = amazon_df.sort_values(by = ['similarity'], ascending = False).head(10)[['Title', 'Description','Category']]
#   return res


# print(search_product(' PURELL ES8 Professional HEALTHY SOAP Foam Refill, Fresh Scent Fragrance, 1200 mL Soap Refill for PURELL ES8 Touch-Free Dispenser (Pack of 2) - 7777-02 '))

# # search_product(' Nickelodeon Teenage Mutant Ninja Turtles Soft Microfiber Full 4 Piece Sheet Set ')

# # web app
# from PIL import Image

# img = Image.open(r'C:\Users\Lenovo\Downloads\amazon_photo_final.jpg')


# st.image(img, width= 600)
# st.title("search engine and product reccomendation system on data")

