import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

def load_data(file_path):
    """
    Load data from a CSV file.
    """
    return pd.read_csv(file_path)

def train_model(X_train, y_train):
    """
    Train a Naive Bayes model.
    """
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model and print the accuracy and classification report.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
    print("Classification Report:")
    print(report)

if __name__ == "__main__":
    # File paths
    data_file_path = 'data/cleaned_tweets.csv'

    # Load data
    df = load_data(data_file_path)
    print(f"Loaded data with {len(df)} records")

    # Prepare data for machine learning
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['tweet'])
    y = df['sentiment']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

