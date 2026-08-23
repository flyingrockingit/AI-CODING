import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv('imdb_top_1000.csv')
df['combined' ] = df['Genre'].fillna('') + ' '+ df['Overview' ]. fillna('')

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])
similarity=cosine_similarity(tfidf_matrix)

def recommend (genre, mood):
    mood_score = TextBlob(mood).sentiment.polarity
    filtered = df[df['Genre'].str.contains(genre, case=False, na=False)]

    recs =[]
    for i , row in filtered.iterrows():
        if pd.isna(row['Overview']):
            continue
        movie_score = TextBlob (row['Overview']).sentiment.polarity 
        if mood_score>= 0 and movie_score>= 0:
            recs.append(row['Series_Title'])
        elif mood_score < 0 and movie_score < 0:
            recs.append(row['Series_Title'])
        if len (recs) == 5:
            break 
        return recs 


genre_input = input ("Enter a genre of your choice:")
mood_input = input ("How are you feeling today dear?")
results = recommend (genre_input, mood_input)
print("\nRecommended Movies:")
for movie in results:
    print(movie)