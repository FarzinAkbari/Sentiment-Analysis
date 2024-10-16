# Sentiment Analysis of Tweets

This project aims to perform sentiment analysis on tweets using Python. The analysis involves fetching tweets through the Twitter API, analyzing their sentiment using TextBlob, and employing machine learning models to enhance the accuracy of sentiment classification.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary libraries.

```bash
pip install tweepy textblob scikit-learn pandas
```
 ## Usage 

 1. Clone the repository:
    
    ```bash
    git clone git@github.com:farzinakbari/Sentiment-Analysis-Tweets.git
    cd Sentiment-Analysis-Tweets
    ```
 2. Edit the `sentiment_analysis_ml.py` file to include your Twitter API credentials.
 3. Run the sentiment analysis script:
    ```bash
    python sentiment_analysis_ml.py
    ```
## Project Structure

```
Sentiment-Analysis-Tweets/
├── data/
├── scripts/
│   └── sentiment_analysis_ml.py
├── .gitignore
├── README.md
└── requirements.txt

```
* `data/`: Directory for storing data files.
* `scripts/`: Directory for storing scripts.
* `sentiment_analysis_ml.py`: Main script for performing sentiment analysis.
* `.gitignore`: File specifying which files should be ignored by Git.
* `README.md`: Project documentation.
* `requirements.txt`: List of required Python packages

## Results
The script outputs the accuracy of the machine learning model and a classification report summarizing the performance. Make sure to check the terminal output to evaluate the results.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Contributions of any kind are appreciated!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
* [Tweepy](https://www.tweepy.org/?form=MG0AV3)
* [TextBlob](https://textblob.readthedocs.io/en/dev/?form=MG0AV3)
* [Scikit-learn](https://scikit-learn.org/stable/)


