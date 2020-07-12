# Multi-Class Text Emotion Analysis
Text-Emotion-Analysis is a project to develop rule-based and deep learning algorithms with an aim to first appropriately detect the different types of emotions contained in a collection of English sentences or a large paragraph and then accurately predict the overall emotion of the paragraph. 

### I have two training and validation dataset:
1. [emotion_data.csv](cleaned_data/emotion_data.csv) in which basic pre-processing of tweets in done (no lemmatization, no removal of stopwords).<br>
This dataset is comprised of <b>55,774</b> tweets from Twitter with labelled emotions of five classes: <b>Neutral, Happy, Sad, Love, Anger</b>.

2. [emotion_data_prep.csv](cleaned_data/emotion_data_prep.csv) in which more deep pre-processing of tweets in done (lemmatization, removal of stopwords, etc).<br>
This dataset is comprised of <b>62,015</b> tweets from Twitter with labelled emotions of five classes: <b>Neutral, Happy, Sad, Love, Anger</b>.


## Comparison of DL and ML models:

### DL:
1. The <b>[DLModel](DLModel.ipynb)</b> using [emotion_data.csv](cleaned_data/emotion_data.csv) gave me <b>64.80%</b> accuracy.

#### Confusion Matrix:

<img src = "https://github.com/kanchitank/Text-Emotion-Analysis/blob/master/images/ConfusionMatrix.JPG" width="700">



2. The <b>[DLModel-Prep](DLModel-Prep.ipynb)</b> using [emotion_data_prep.csv](cleaned_data/emotion_data_prep.csv) gave me <b>63.47%</b> accuracy.

#### Confusion Matrix (Prep):

<img src = "https://github.com/kanchitank/Text-Emotion-Analysis/blob/master/images/ConfusionMatrixPrep.JPG" width="700">



### ML:
The <b>ML Algorithms</b> used for prediction are listed as follows:

#### Building models using different classifiers (Count vectorizer): 

Model 1: <b>Multinomial Naive Bayes Classifier</b> - Accuracy <b>58.46%</b><br>
Model 2: <b>Linear SVM</b> - Accuracy <b>62.00%</b><br>
Model 3: <b>Logistic Regression</b> - Accuracy <b>62.47%</b>

#### Building models using different classifiers (TF-IDF vectorizer): 

Model 1: <b>Multinomial Naive Bayes Classifier</b> - Accuracy <b>38.37%</b><br>
Model 2: <b>Linear SVM</b> - Accuracy <b>38.49%</b><br>
Model 3: <b>Logistic Regression</b> - Accuracy <b>40.13%</b>



### Prediction of emotions from paragraphs and sentences (DL Model):


![](images/Predictions.JPG)
