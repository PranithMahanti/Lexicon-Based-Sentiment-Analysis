# Lexicon-Based-Sentiment-Analysis
- Used in NLP to detect sentiment in a piece of text.
- It uses lists of words and phrases that are linked to different emotions to label the words (e.g. positive, negative, or neutral) and detect sentiment.
- A popular way to calculate Sentiment Score: 
  ### $StScore = \Delta EW / Total$
  where, $\Delta EW = (no. of positive words - no. of negative words)$
			
- Polarity of a text is given by a decimal (float) value in the range of [-1,1]. It denotes the positivity of the tone of the given sentence.
	- Pol < 0 : Negative
	- Pol = 0 : Neutral
	- Pol > 0 : Positive

## Pre-processing Data
1. Removal of all special characters and punctuation marks.
2. Removal of stop words.
	- Stop words are the words in a stop list which are filtered out before or after processing of natural language data because they are deemed to have little semantic value.
	- List of stop words:\
    	https://countwordsfree.com/stopwords 
   	- A simple demonstration of removal of stop words with NLTK in Python:\
   		https://www.geeksforgeeks.org/nlp/removing-stop-words-nltk-python/
3. Expansion of word contractions
4. Tokenisation of the sentences:
	- Converting sentences into words
5. Case uniformity:
	- All the words are converted into UPPER or lower case.
6. Stemming and Lemmatisation:
	- Converting a word into its base form, which is known as lemma in computational linguistics.

## Differences between Stemming and Lemmatization:
	
| **Stemming**                                                                                                                                           | **Lemmatization**                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stemmers eliminate word suffixes by running input word tokens against a pre-defined list of common suffixes.                                           | Lemmatization will reduce morphological variants to one dictionary base form.                                                                               |
| The stemmer then removes any found suffix character strings from the word, should the latter not defy any rules or conditions attached to that suffix. | Lemmatization ensures the output word is an existing normalized form of the word                                                                            |
| **Text:**  <br>“The company was investing heavily in renewable energy solutions.” <br>**Tokens:** <br>the, compani, wa, invest, heavili, in, renew, energi, solut  | **Text:** <br>“The company was investing heavily in renewable energy solutions.” <br>**Tokens:** <br>the, company, be, invest, heavily, in, renewable, energy, solution |

*In most cases we prefer Lemmatization over stemming because the former conducts a morphological analysis of words, thus resulting in more accurate word roots.*

- **Precision** = number of true positives / all positives
- **Recall** = True positives / ( True Positives + False Negatives)
- **F1 Score** = 2 * (Precision *Recall) / (Precision + Recall)

## Popular Lexicons
1. **AFINN Lexicon:** \
 		- The current version is AFINN-en-165.txt and it contains 3382 words along with its polarity score.
2. **SentiWordNet:**
 		- Lexical resource for opinion mining. \ SentiWordNet assigns to each synset of WordNet three sentiment scores: positivity, negativity, objectivity.
3. **VADER:** \
 		- An open-source, NLTK-integrated sentiment analysis tool, is specifically designed for social media sentiments and can be applied directly to unlabelled text. \
   		- **VADER** is capable of detection of polarity and intensity of emotion.

## Extracting Features
Before training the data with SVM and Logistic Regression we need to convert data to feature vectors. We use Count Vectorizer and TF-IDF Vectorizer for the same.
1. **BOW - Bag of Words Model**
	- A bag-of-words model, or BoW for short, is a way of extracting features from text for use in modeling, such as with machine learning algorithms.
2. **Scoring Words**
	- **Counts**: Count the number of times each word appears in a document.
	- **Frequencies**: Calculate the frequency that each word appears in a document out of all the words in the document.
3. **TF-IDF (Term Frequency-Inverse Document Frequency)**
	- More importance to words that occur more frequently in a document than to words with lesser occurrence. 
	- **TF** = freq. of a word/total words.
	- **IDF** = ln(total no. of docs/no. of docs containing that word)

*In the [Source 2](https://medium.com/nerd-for-tech/sentiment-analysis-lexicon-models-vs-machine-learning-b6e3af8fe746) mentioned below, the author points out that the AFINN lexical model has better accuracy (72%) than other lexical models, though they were performing close enough to it.
And in case of Supervised Learning models Logistic Regression model on Bag of Word model features, is the best as it is having an accuracy of 89.94%.*


## Sources used:
1. https://www.knime.com/blog/lexicon-based-sentiment-analysis
2. https://medium.com/nerd-for-tech/sentiment-analysis-lexicon-models-vs-machine-learning-b6e3af8fe746
3. https://www.ibm.com/think/topics/stemming-lemmatization
4. https://www.ibm.com/think/topics/stemming-lemmatization
	- This article also has code samples that show stemming and lemmatisation in Python using NLTK. Check that out too.
5. https://machinelearningmastery.com/gentle-introduction-bag-words-model/
6. https://medium.com/greyatom/an-introduction-to-bag-of-words-in-nlp-ac967d43b428
7. https://numerous.ai/blog/lexicon-based-sentiment-analysis
	- This blog explains the Lexicon-based Sentiment Analysis in a detailed fashion and has a lot of other Related Reads.


## Research papers:
(**Disclaimer**: I haven’t read all these research papers but I have heard that they were useful to others doing similar projects)
1. https://ijrti.org/papers/IJRTI2312113.pdf
2. https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2010.01625.x
	- This is the Loughran–McDonald (2011) lexicon, which is considered the golden standard for these kinds of projects in finance. 
	- Shows how domain-specific lexicons outperform generic ones.
3. https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2007.01232.x
	- Used a lexicon-based approach to classify Wall Street Journal column text.


## Contributors
- [Pranith Mahanti](https://github.com/PranithMahanti/)
- [Dandu Asrith](https://github.com/asrith-306/)
