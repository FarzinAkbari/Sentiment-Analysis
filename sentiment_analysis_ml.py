import tweepy
import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Search for tweets containing the keyword
public_tweets = api.search(q='keyword', count=100)

tweets_data = []
for tweet in public_tweets:
    # Analyze the sentiment of the tweet
    analysis = TextBlob(tweet.text)
    sentiment = 'positive' if analysis.sentiment.polarity > 0 else 'negative'
    tweets_data.append({'tweet': tweet.text, 'sentiment': sentiment})

# Create a DataFrame from the tweets data
df = pd.DataFrame(tweets_data)

# Prepare data for machine learning
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['tweet'])
y = df['sentiment']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

