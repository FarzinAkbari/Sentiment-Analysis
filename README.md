DD# Sentiment Analysis of Tweets

This project aims to perform sentiment analysis on tweets using Python. The analysis involves fetching tweets through the Twitter API, analyzing their sentiment using TextBlob, and employing machine learning models to enhance the accuracy of sentiment classification.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary libraries.

```bash
pip install -r requirements.txt
```
 ## Usage 

 1. Clone the repository:
    
    ```bash
    git clone git@github.com:farzinakbari/Sentiment-Analysis-Tweets.git
    cd Sentiment-Analysis-Tweets
    ```
 2. Edit the `scripts/sentiment_analysis_ml.py` file to include your Twitter API credentials.
 3. Run the data processing script to clean the tweets:
    ```bash
    python scripts/data_processing.py
    ```
 4. Run the model training script to train the machine learning model:
    ```bash
	python scripts/model_training.py
    ```  

## Project Structure

```Sentiment-Analysis-Tweets/
Sentiment-Analysis-Tweets/
├── data/
│   └── tweets.csv
│   └── cleaned_tweets.csv
├── scripts/
│   └── sentiment_analysis_ml.py
│   └── data_processing.py
│   └── model_training.py
├── .gitignore
├── README.md
└── requirements.txt


```
* `data/`: Directory for storing data files.
* `scripts/`: Directory for storing scripts.
* `sentiment_analysis_ml.py`: Main script for performing sentiment analysis.
* `data_processing.py`: Script for cleaning and processing data.
* `model_training.py`: Script for training machine learning model.
* `.gitignore`: File specifying which files should be ignored by Git.
* `README.md`: Project documentation.
* `requirements.txt`: List of required Python packages

## Results
The script outputs the accuracy of the machine learning model and a classification report summarizing the performance. Make sure to check the terminal output to evaluate the results.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Contributions of any kind are appreciated!

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/FarzinAkbari/Sentiment-Analysis-Tweets/blob/main/LICENSE) file for details.

## Acknowledgments
* [Tweepy](https://www.tweepy.org/?form=MG0AV3)
* [TextBlob](https://textblob.readthedocs.io/en/dev/?form=MG0AV3)
* [Scikit-learn](https://scikit-learn.org/stable/)


## Examples

### Running Sentiment Analysis

To perform sentiment analysis on tweets, follow these steps:

1. Fetch tweets using your Twitter API credentials and save them in `data/tweets.csv`.
2. Run the data processing script to clean the tweets:
   ```bash
   python scripts/data_processing.py
   ```
3. Train the machine learning model using the cleaned tweets:
   ```bash
   python scripts/model_training.py
   ```

## Contributing

We welcome contributions! Here are some ways you can contribute:

- **Reporting Bugs:** If you find any bugs, please open an issue on GitHub.
- **Improving Documentation:** If you find any errors or have suggestions for improvements, feel free to open a pull request.
- **Adding Features:** If you have new features or improvements, please open a pull request with a description of the changes.

Before contributing, please make sure to read our [Code of Conduct](CODE_OF_CONDUCT.md).


## Algorithm Explanation

### Sentiment Analysis

We use the `TextBlob` library to perform sentiment analysis on tweets. `TextBlob` uses a combination of machine learning techniques and lexicon-based approaches to determine the sentiment of a given text.

### Machine Learning Model

We train a Naive Bayes classifier using the `scikit-learn` library to improve the accuracy of sentiment classification. The model is trained on a dataset of cleaned tweets and is evaluated using standard metrics such as accuracy and classification report.


